#!/usr/bin/env python3
"""
Model Router Background Service

Continuously monitors and applies automatic model switching.
Runs as a background daemon.

Usage:
    # Start service
    python3 model-router-service.py start
    
    # Stop service  
    python3 model-router-service.py stop
    
    # Check status
    python3 model-router-service.py status
"""

import json
import sys
import os
import time
import signal
import atexit
from pathlib import Path
from datetime import datetime
from typing import Optional

# Get script directory
SCRIPT_DIR = Path(__file__).parent.resolve()
os.chdir(SCRIPT_DIR)
sys.path.insert(0, str(SCRIPT_DIR))

# Import router
from model_router import ModelRouter


class ModelRouterService:
    """Background service for automatic model switching."""
    
    def __init__(self):
        """Initialize the service."""
        self.pid_file = Path('/tmp/model-router.pid')
        self.log_file = Path('/tmp/model-router-service.log')
        self.running = False
        self.router = None
        
        # Register cleanup
        atexit.register(self.cleanup)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        print(f"🤖 Model Router Service initialized")
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals."""
        print(f"\n👋 Received signal {signum}, shutting down...")
        self.running = False
    
    def cleanup(self):
        """Clean up on exit."""
        if self.pid_file.exists():
            self.pid_file.unlink()
            print(f"🧹 PID file removed")
    
    def write_pid(self):
        """Write PID file."""
        with open(self.pid_file, 'w') as f:
            f.write(str(os.getpid()))
        print(f"📝 PID {os.getpid()} written to {self.pid_file}")
    
    def is_running(self) -> bool:
        """Check if service is already running."""
        if not self.pid_file.exists():
            return False
        
        try:
            with open(self.pid_file, 'r') as f:
                pid = int(f.read().strip())
            
            # Check if process exists
            os.kill(pid, 0)
            return True
        except (ProcessLookupError, ValueError):
            # PID file exists but process not running
            self.pid_file.unlink()
            return False
    
    def get_pid(self) -> Optional[int]:
        """Get PID of running service."""
        if not self.pid_file.exists():
            return None
        
        try:
            with open(self.pid_file, 'r') as f:
                return int(f.read().strip())
        except:
            return None
    
    def log(self, message: str):
        """Log message to file and console."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        
        # Console
        print(log_entry)
        
        # File
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def start(self):
        """Start the background service."""
        if self.is_running():
            pid = self.get_pid()
            print(f"❌ Service already running (PID: {pid})")
            return
        
        self.log("🚀 Starting Model Router Service...")
        self.write_pid()
        
        # Initialize router
        self.router = ModelRouter()
        self.running = True
        
        self.log("✅ Service started")
        self.log("📊 Monitoring for requests...")
        
        # Main loop
        try:
            while self.running:
                # Check for requests (placeholder - would integrate with OpenClaw)
                time.sleep(5)
        
        except KeyboardInterrupt:
            self.log("👋 Interrupted by user")
        except Exception as e:
            self.log(f"❌ Error: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the service."""
        self.log("🛑 Stopping Model Router Service...")
        self.running = False
        
        if self.pid_file.exists():
            self.pid_file.unlink()
        
        self.log("✅ Service stopped")
    
    def status(self):
        """Show service status."""
        print("\n" + "="*60)
        print("🤖 MODEL ROUTER SERVICE STATUS")
        print("="*60)
        
        if self.is_running():
            pid = self.get_pid()
            print(f"✅ Status: RUNNING")
            print(f"📊 PID: {pid}")
            print(f"📝 Log: {self.log_file}")
        else:
            print(f"❌ Status: STOPPED")
        
        # Show recent logs
        if self.log_file.exists():
            print(f"\n📋 Recent Logs:")
            with open(self.log_file, 'r') as f:
                lines = f.readlines()[-5:]
                for line in lines:
                    print(f"  {line.strip()}")
        
        print("="*60 + "\n")
    
    def restart(self):
        """Restart the service."""
        self.stop()
        time.sleep(1)
        self.start()


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 model-router-service.py [start|stop|status|restart]")
        sys.exit(1)
    
    service = ModelRouterService()
    
    command = sys.argv[1].lower()
    
    if command == 'start':
        service.start()
    elif command == 'stop':
        service.stop()
    elif command == 'status':
        service.status()
    elif command == 'restart':
        service.restart()
    else:
        print(f"❌ Unknown command: {command}")
        print("Usage: python3 model-router-service.py [start|stop|status|restart]")
        sys.exit(1)


if __name__ == '__main__':
    main()
