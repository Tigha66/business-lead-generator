#!/usr/bin/env python3
"""
Model Router - Automatic Model Selection Based on Request Type

Analyzes user input and selects the best model for the task.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta


class ModelRouter:
    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = Path(__file__).parent / 'model-router.json'
        
        self.config = self.load_config(config_path)
        self.conversation_history = {}  # Track model usage per conversation
        self.last_used = {}  # Track last model used per session
        
    def load_config(self, config_path: str) -> Dict:
        """Load model router configuration."""
        path = Path(config_path)
        if not path.exists():
            print(f"⚠️  Config not found: {path}")
            return self.get_default_config()
        
        with open(path, 'r') as f:
            return json.load(f)
    
    def get_default_config(self) -> Dict:
        """Return default configuration."""
        return {
            "routing": {
                "enabled": True,
                "default": "bailian/qwen3.5-plus",
                "categories": {
                    "general": {
                        "model": "bailian/qwen3.5-plus",
                        "triggers": [],
                        "default": True
                    }
                }
            }
        }
    
    def select_model(self, user_input: str, has_image: bool = False, 
                    session_id: str = "default") -> Dict:
        """
        Select the best model based on user input.
        
        Args:
            user_input: The user's message/request
            has_image: Whether the request includes an image
            session_id: Session identifier for conversation tracking
        
        Returns:
            Dict with selected model and reasoning
        """
        routing = self.config.get('routing', {})
        
        if not routing.get('enabled', True):
            return {
                "model": routing.get('default', 'bailian/qwen3.5-plus'),
                "reason": "Routing disabled",
                "category": "general"
            }
        
        # Check if we should stick with current model for ongoing conversation
        if self.should_stick_with_model(session_id):
            current_model = self.last_used.get(session_id, routing['default'])
            return {
                "model": current_model,
                "reason": "Continuing conversation with current model",
                "category": "conversation-continuity"
            }
        
        # Check for image input first (highest priority)
        if has_image:
            vision_config = routing['categories'].get('vision', {})
            return {
                "model": vision_config.get('model', 'bailian/kimi-k2.5'),
                "fallback": vision_config.get('fallback', 'dashscope/qwen3-vl-plus'),
                "reason": "Image input detected",
                "category": "vision"
            }
        
        # Analyze input and categorize
        category, confidence, matched_triggers = self.categorize_input(user_input)
        
        # Get model for category
        category_config = routing['categories'].get(category, {})
        selected_model = category_config.get('model', routing['default'])
        fallback_model = category_config.get('fallback', routing['default'])
        
        # Track usage
        self.last_used[session_id] = selected_model
        self.conversation_history[session_id] = {
            "category": category,
            "model": selected_model,
            "timestamp": datetime.now()
        }
        
        return {
            "model": selected_model,
            "fallback": fallback_model,
            "reason": f"Detected {category} task (confidence: {confidence:.0%})",
            "category": category,
            "matched_triggers": matched_triggers
        }
    
    def categorize_input(self, user_input: str) -> Tuple[str, float, List[str]]:
        """
        Categorize user input and return best matching category.
        
        Returns:
            Tuple of (category, confidence, matched_triggers)
        """
        input_lower = user_input.lower()
        categories = self.config.get('routing', {}).get('categories', {})
        
        best_match = None
        best_confidence = 0.0
        best_triggers = []
        
        for category_name, category_config in categories.items():
            # Skip default category in initial matching
            if category_config.get('default', False):
                continue
            
            triggers = category_config.get('triggers', [])
            matched = []
            
            for trigger in triggers:
                # Check for exact trigger match
                if trigger.lower() in input_lower:
                    matched.append(trigger)
                # Check for regex patterns (if trigger starts with regex:)
                elif trigger.startswith('regex:'):
                    pattern = trigger[6:]  # Remove 'regex:' prefix
                    if re.search(pattern, input_lower):
                        matched.append(f"regex:{pattern}")
            
            # Calculate confidence based on number of matches
            if matched:
                confidence = min(1.0, len(matched) * 0.25)  # Max 4 matches = 100% confidence
                
                # Boost confidence for priority categories
                priority = category_config.get('priority', 99)
                if priority <= 3:  # High priority categories
                    confidence = min(1.0, confidence + 0.1)
                
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_match = category_name
                    best_triggers = matched
        
        # If no match found, use default
        if not best_match:
            for category_name, category_config in categories.items():
                if category_config.get('default', False):
                    return (category_name, 0.5, [])
            
            return ("general", 0.5, [])
        
        return (best_match, best_confidence, best_triggers)
    
    def should_stick_with_model(self, session_id: str) -> bool:
        """Check if we should continue using the current model for this session."""
        rules = self.config.get('rules', {})
        
        if not rules.get('stickWithModelForConversation', True):
            return False
        
        if session_id not in self.conversation_history:
            return False
        
        last_used = self.conversation_history[session_id].get('timestamp')
        if not last_used:
            return False
        
        # Convert string timestamp back to datetime if needed
        if isinstance(last_used, str):
            last_used = datetime.fromisoformat(last_used)
        
        window_minutes = rules.get('conversationWindowMinutes', 30)
        time_diff = datetime.now() - last_used
        
        return time_diff < timedelta(minutes=window_minutes)
    
    def get_model_info(self, model_id: str) -> Dict:
        """Get information about a specific model."""
        capabilities = self.config.get('modelCapabilities', {})
        return capabilities.get(model_id, {
            "name": model_id,
            "supportsImages": False,
            "contextWindow": "unknown",
            "speed": "unknown",
            "quality": "unknown"
        })
    
    def list_available_models(self) -> List[Dict]:
        """List all available models with their capabilities."""
        capabilities = self.config.get('modelCapabilities', {})
        return [
            {
                "id": model_id,
                **info
            }
            for model_id, info in capabilities.items()
        ]
    
    def print_selection(self, selection: Dict):
        """Pretty print model selection for debugging."""
        print("\n" + "="*60)
        print("🤖 MODEL ROUTER SELECTION")
        print("="*60)
        print(f"📦 Selected Model: {selection['model']}")
        if selection.get('fallback'):
            print(f"🔄 Fallback: {selection['fallback']}")
        print(f"🎯 Category: {selection['category']}")
        print(f"💡 Reason: {selection['reason']}")
        if selection.get('matched_triggers'):
            print(f"🔑 Matched: {', '.join(selection['matched_triggers'][:5])}")
        print("="*60 + "\n")


# CLI Interface
if __name__ == '__main__':
    import sys
    
    router = ModelRouter()
    
    if len(sys.argv) > 1:
        # Test mode: pass input as argument
        test_input = ' '.join(sys.argv[1:])
        has_image = '--image' in sys.argv
        session_id = 'cli-test'
        
        selection = router.select_model(test_input, has_image, session_id)
        router.print_selection(selection)
    else:
        # Interactive mode
        print("🤖 Model Router - Interactive Test Mode")
        print("Type your request (or 'quit' to exit)")
        print("Add '--image' to simulate image input\n")
        
        session_id = f"session-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                has_image = '--image' in user_input
                clean_input = user_input.replace('--image', '').strip()
                
                selection = router.select_model(clean_input, has_image, session_id)
                router.print_selection(selection)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
