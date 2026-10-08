#!/usr/bin/env python3
"""
Aqfal - Safe Web Blocking System
Admin Login Module
Password: Aqfal@2026Secure!
"""

import hashlib
import getpass
import json
from datetime import datetime
import os

# Admin Credentials - ENCRYPTED
ADMIN_USER = "admin"
ADMIN_PASS_HASH = hashlib.sha256("Aqfal@2026Secure!".encode()).hexdigest()

class SecureLogin:
    def __init__(self):
        self.max_attempts = 3
        self.attempt_count = 0
        self.logs_file = "security_logs.json"
    
    def hash_password(self, password):
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def log_attempt(self, username, status):
        """Log login attempts"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "username": username,
            "status": status,
            "ip": "127.0.0.1"
        }
        try:
            with open(self.logs_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except:
            pass
    
    def login(self):
        """Secure admin login"""
        print("\n" + "="*60)
        print("🔐 AQFAL - SAFE WEB BLOCKING SYSTEM")
        print("Secure Admin Login")
        print("="*60 + "\n")
        
        while self.attempt_count < self.max_attempts:
            try:
                username = input("👤 Admin Username: ").strip()
                password = getpass.getpass("🔑 Password: ")
                
                if username == ADMIN_USER and self.hash_password(password) == ADMIN_PASS_HASH:
                    print("\n✅ Login Successful!")
                    print(f"🎯 Welcome, Admin!\n")
                    self.log_attempt(username, "SUCCESS")
                    return True
                else:
                    self.attempt_count += 1
                    remaining = self.max_attempts - self.attempt_count
                    print(f"\n❌ Invalid credentials!")
                    print(f"⚠️  Attempts remaining: {remaining}\n")
                    self.log_attempt(username, "FAILED")
            except KeyboardInterrupt:
                print("\n\n🚫 Login cancelled.")
                return False
        
        print("\n🚨 Access Denied! Too many failed attempts.")
        print("⏳ Please try again later.\n")
        return False

if __name__ == "__main__":
    login_system = SecureLogin()
    if login_system.login():
        print("✨ Proceeding to Admin Panel...\n")
    else:
        print("\n🔒 System locked.\n")
