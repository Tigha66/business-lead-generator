#!/usr/bin/env python3
"""
OpenClaw Auto Model Switch Integration

Automatically selects the best model for each user request.
Integrates with OpenClaw sessions for seamless model switching.

Usage:
    from auto_model_switch import OpenClawModelRouter
    
    router = OpenClawModelRouter()
    
    # For each user message
    response = router.route_message(
        user_input="help me write python code",
        session_id="session-123",
        has_image=False
    )
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

# Add workspace to path
sys.path.insert(0, str(Path(__file__).parent))

from model_router import ModelRouter


class OpenClawModelRouter:
    """
    OpenClaw integration for automatic model switching.
    
    Monitors user messages and automatically selects the best model
    for each request based on content analysis.
    """
    
    def __init__(self, config_path: str = None):
        """Initialize the OpenClaw Model Router."""
        self.router = ModelRouter(config_path)
        self.session_models = {}  # Track model per session
        self.log_file = Path(__file__).parent / 'model-router-usage.log'
        
        # Load OpenClaw config
        self.openclaw_config_path = Path.home() / '.openclaw' / 'openclaw.json'
        self.openclaw_config = self.load_openclaw_config()
        
        print(f"✅ OpenClaw Model Router initialized")
        print(f"📊 Default model: {self.get_default_model()}")
        print(f"📝 Logging to: {self.log_file}")
    
    def load_openclaw_config(self) -> Dict:
        """Load OpenClaw configuration."""
        if not self.openclaw_config_path.exists():
            print(f"⚠️  OpenClaw config not found: {self.openclaw_config_path}")
            return {}
        
        with open(self.openclaw_config_path, 'r') as f:
            return json.load(f)
    
    def get_default_model(self) -> str:
        """Get the current default model from OpenClaw config."""
        try:
            return self.openclaw_config.get('agents', {}).get('defaults', {}).get(
                'model', {}
            ).get('primary', 'bailian/qwen3.5-plus')
        except:
            return 'bailian/qwen3.5-plus'
    
    def set_session_model(self, session_id: str, model: str):
        """
        Set the model for a specific OpenClaw session.
        
        This would integrate with OpenClaw's session management.
        For now, it logs the selection.
        """
        self.session_models[session_id] = model
        
        # Log the selection
        self.log_selection(session_id, model)
        
        # In production, this would call OpenClaw's API to update the session
        print(f"🎯 Session {session_id}: Using {model}")
    
    def route_message(self, user_input: str, session_id: str = "default", 
                     has_image: bool = False) -> Dict:
        """
        Route a user message to the appropriate model.
        
        Args:
            user_input: The user's message
            session_id: OpenClaw session ID
            has_image: Whether the message includes an image
        
        Returns:
            Dict with selected model and routing info
        """
        # Select best model
        selection = self.router.select_model(user_input, has_image, session_id)
        
        # Set model for this session
        self.set_session_model(session_id, selection['model'])
        
        return selection
    
    def log_selection(self, session_id: str, model: str):
        """Log model selection to file."""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] Session: {session_id} → Model: {model}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
    
    def get_session_info(self, session_id: str) -> Dict:
        """Get information about a session's model usage."""
        return {
            "session_id": session_id,
            "current_model": self.session_models.get(session_id, "not set"),
            "default_model": self.get_default_model()
        }
    
    def print_status(self):
        """Print current router status."""
        print("\n" + "="*60)
        print("🤖 OPENCLAW MODEL ROUTER STATUS")
        print("="*60)
        print(f"📦 Default Model: {self.get_default_model()}")
        print(f"📊 Active Sessions: {len(self.session_models)}")
        print(f"📝 Log File: {self.log_file}")
        print(f"📁 Config: {self.openclaw_config_path}")
        
        if self.session_models:
            print("\n📋 Active Sessions:")
            for session_id, model in self.session_models.items():
                print(f"  • {session_id}: {model}")
        
        print("="*60 + "\n")
    
    def update_openclaw_config(self, model: str):
        """
        Update OpenClaw's default model configuration.
        
        Args:
            model: The model ID to set as default
        """
        if not self.openclaw_config_path.exists():
            print(f"❌ OpenClaw config not found")
            return
        
        # Update config
        if 'agents' not in self.openclaw_config:
            self.openclaw_config['agents'] = {}
        if 'defaults' not in self.openclaw_config['agents']:
            self.openclaw_config['agents']['defaults'] = {}
        if 'model' not in self.openclaw_config['agents']['defaults']:
            self.openclaw_config['agents']['defaults']['model'] = {}
        
        self.openclaw_config['agents']['defaults']['model']['primary'] = model
        
        # Backup existing config
        backup_path = self.openclaw_config_path.with_suffix('.json.bak')
        import shutil
        shutil.copy2(self.openclaw_config_path, backup_path)
        print(f"💾 Backup created: {backup_path}")
        
        # Write updated config
        with open(self.openclaw_config_path, 'w') as f:
            json.dump(self.openclaw_config, f, indent=2)
        
        print(f"✅ OpenClaw config updated: {model}")
        print(f"⚠️  Restart gateway for changes to take effect:")
        print(f"   openclaw gateway restart")


# CLI Interface
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='OpenClaw Auto Model Router')
    parser.add_argument('--test', type=str, help='Test with a message')
    parser.add_argument('--session', type=str, default='test-session', 
                       help='Session ID')
    parser.add_argument('--image', action='store_true', help='Has image')
    parser.add_argument('--status', action='store_true', help='Show status')
    parser.add_argument('--set-default', type=str, help='Set default model')
    
    args = parser.parse_args()
    
    router = OpenClawModelRouter()
    
    if args.set_default:
        router.update_openclaw_config(args.set_default)
    
    elif args.status:
        router.print_status()
    
    elif args.test:
        print(f"\n💬 Testing: '{args.test}'")
        print(f"📋 Session: {args.session}")
        print(f"🖼️  Image: {args.image}\n")
        
        selection = router.route_message(args.test, args.session, args.image)
        router.router.print_selection(selection)
        
        print(f"\n✅ Session model set to: {selection['model']}")
    
    else:
        print("🤖 OpenClaw Auto Model Router")
        print("="*60)
        print("\nUsage:")
        print("  python3 auto-model-switch.py --test 'your message'")
        print("  python3 auto-model-switch.py --status")
        print("  python3 auto-model-switch.py --set-default 'model-id'")
        print("\nExamples:")
        print("  python3 auto-model-switch.py --test 'help me code'")
        print("  python3 auto-model-switch.py --test 'analyze this' --session session-1")
        print("  python3 auto-model-switch.py --status")
        print("="*60)
