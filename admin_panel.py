#!/usr/bin/env python3
"""
Aqfal - Admin Control Panel
Manage blocked websites and security settings
"""

import json
import os
from datetime import datetime
from login import SecureLogin

class AqfalAdminPanel:
    def __init__(self):
        self.blocked_sites_file = "blocked_sites.json"
        self.config_file = "aqfal_config.json"
        self.admin_name = "Admin"
        self.load_or_create_database()
    
    def load_or_create_database(self):
        """Load or create blocked sites database"""
        if not os.path.exists(self.blocked_sites_file):
            self.blocked_sites = []
            self.save_database()
        else:
            with open(self.blocked_sites_file, "r") as f:
                self.blocked_sites = json.load(f)
    
    def save_database(self):
        """Save blocked sites to database"""
        with open(self.blocked_sites_file, "w") as f:
            json.dump(self.blocked_sites, f, indent=2)
    
    def display_menu(self):
        """Display admin menu"""
        print("\n" + "="*60)
        print("🛡️  AQFAL ADMIN CONTROL PANEL")
        print("Safe Web Blocking System")
        print("="*60)
        print("\n📋 Available Commands:\n")
        print("1️⃣  ➕ Add Website to Block List")
        print("2️⃣  ➖ Remove Website from Block List")
        print("3️⃣  📊 View All Blocked Sites")
        print("4️⃣  🔍 Search Blocked Sites")
        print("5️⃣  📈 View Statistics")
        print("6️⃣  🧹 Clear All Blocked Sites")
        print("7️⃣  💾 Export Block List")
        print("8️⃣  📥 Import Block List")
        print("9️⃣  🚪 Logout\n")
        print("="*60 + "\n")
    
    def add_site(self):
        """Add website to block list"""
        print("\n➕ Add Website to Block List\n")
        url = input("Enter website URL (e.g., example.com): ").strip().lower()
        reason = input("Reason for blocking (optional): ").strip()
        
        if not url:
            print("❌ URL cannot be empty!")
            return
        
        if url in self.blocked_sites:
            print(f"⚠️  {url} is already blocked!")
            return
        
        site_entry = {
            "url": url,
            "reason": reason or "Security",
            "added_date": datetime.now().isoformat(),
            "status": "active"
        }
        
        self.blocked_sites.append(site_entry)
        self.save_database()
        print(f"\n✅ {url} has been added to block list!\n")
    
    def remove_site(self):
        """Remove website from block list"""
        print("\n➖ Remove Website from Block List\n")
        url = input("Enter website URL to remove: ").strip().lower()
        
        for i, site in enumerate(self.blocked_sites):
            if site["url"] == url:
                removed = self.blocked_sites.pop(i)
                self.save_database()
                print(f"\n✅ {url} has been removed from block list!\n")
                return
        
        print(f"\n❌ {url} not found in block list!\n")
    
    def view_sites(self):
        """View all blocked sites"""
        print("\n📊 Blocked Websites List\n")
        
        if not self.blocked_sites:
            print("No websites blocked yet.\n")
            return
        
        for i, site in enumerate(self.blocked_sites, 1):
            print(f"{i}. {site['url']}")
            print(f"   Reason: {site['reason']}")
            print(f"   Added: {site['added_date']}")
            print()
    
    def search_sites(self):
        """Search in blocked sites"""
        print("\n🔍 Search Blocked Sites\n")
        query = input("Search for: ").strip().lower()
        
        results = [site for site in self.blocked_sites if query in site['url']]
        
        if not results:
            print(f"\nNo results found for '{query}'\n")
            return
        
        print(f"\n✅ Found {len(results)} result(s):\n")
        for site in results:
            print(f"• {site['url']} - {site['reason']}")
        print()
    
    def show_statistics(self):
        """Show blocking statistics"""
        print("\n📈 Blocking Statistics\n")
        total_blocked = len(self.blocked_sites)
        print(f"Total Blocked Sites: {total_blocked}")
        print(f"Active Blocks: {total_blocked}")
        print(f"System Status: ✅ Active\n")
    
    def clear_all(self):
        """Clear all blocked sites"""
        print("\n🧹 Clear All Blocked Sites\n")
        confirm = input("⚠️  Are you sure? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            self.blocked_sites = []
            self.save_database()
            print("\n✅ All blocked sites have been cleared!\n")
        else:
            print("\n❌ Operation cancelled.\n")
    
    def export_list(self):
        """Export block list"""
        print("\n💾 Export Block List\n")
        filename = f"aqfal_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, "w") as f:
            json.dump(self.blocked_sites, f, indent=2)
        
        print(f"✅ Block list exported to {filename}\n")
    
    def import_list(self):
        """Import block list"""
        print("\n📥 Import Block List\n")
        filename = input("Enter filename to import: ").strip()
        
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}\n")
            return
        
        try:
            with open(filename, "r") as f:
                imported_sites = json.load(f)
            
            self.blocked_sites.extend(imported_sites)
            self.save_database()
            print(f"✅ Imported {len(imported_sites)} sites!\n")
        except Exception as e:
            print(f"❌ Error importing file: {e}\n")
    
    def run(self):
        """Run admin panel"""
        while True:
            self.display_menu()
            choice = input("👉 Select option (1-9): ").strip()
            
            if choice == "1":
                self.add_site()
            elif choice == "2":
                self.remove_site()
            elif choice == "3":
                self.view_sites()
            elif choice == "4":
                self.search_sites()
            elif choice == "5":
                self.show_statistics()
            elif choice == "6":
                self.clear_all()
            elif choice == "7":
                self.export_list()
            elif choice == "8":
                self.import_list()
            elif choice == "9":
                print("\n👋 Logging out...\n")
                break
            else:
                print("\n❌ Invalid option! Try again.\n")

if __name__ == "__main__":
    login_system = SecureLogin()
    if login_system.login():
        panel = AqfalAdminPanel()
        panel.run()
    else:
        print("\n🔒 Access Denied!\n")
