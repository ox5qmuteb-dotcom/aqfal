# 🔐 AQFAL - Safe Web Blocking System

**نظام حجب المواقع الآمن**

## 📋 Overview

Aqfal is a comprehensive web blocking system designed for safe internet usage. It provides an easy-to-use admin panel for managing blocked websites and ensuring a secure browsing experience.

## ✨ Features

✅ **Secure Admin Login**
- Password-protected access
- Login attempt logging
- Encrypted credentials

✅ **Website Management**
- Add websites to block list
- Remove websites from block list
- Search through blocked sites
- View complete block list

✅ **Database Management**
- JSON-based storage
- Export/Import functionality
- Backup capabilities

✅ **Statistics & Monitoring**
- View blocking statistics
- Track system status
- Detailed logging

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/ox5qmuteb-dotcom/aqfal.git
cd aqfal
python3 login.py
```

### Login Credentials
```
Username: admin
Password: Aqfal@2026Secure!
```

### First Time Setup
1. Run `python3 login.py`
2. Enter credentials
3. Access admin panel with `python3 admin_panel.py`

## 📁 File Structure

```
aqfal/
├── login.py              # Secure login system
├── admin_panel.py        # Main control panel
├── blocked_sites.json    # Block list database
├── security_logs.json    # Login attempt logs
└── README.md            # This file
```

## 🔑 Security Features

- SHA256 password hashing
- Attempt logging with timestamps
- Secure credential storage
- Session management
- Access control

## 📊 Usage

### Add a Website
```
Select Option 1 → Enter URL → Enter Reason
```

### View Blocked Sites
```
Select Option 3 → View complete list
```

### Export Block List
```
Select Option 7 → Automatic filename generation
```

## ⚙️ Configuration

Default settings in `aqfal_config.json`:
- Max login attempts: 3
- Log retention: Unlimited
- Block list format: JSON

## 🛡️ Safety Guidelines

✅ **Do:**
- Block harmful/malicious websites
- Block adult content
- Block phishing sites
- Protect children online
- Keep password secure

❌ **Don't:**
- Block legitimate educational content
- Use for censorship
- Share login credentials
- Modify files directly

## 📝 Logging

All login attempts are logged to `security_logs.json`:
```json
{
  "timestamp": "2026-10-08T12:00:00",
  "username": "admin",
  "status": "SUCCESS",
  "ip": "127.0.0.1"
}
```

## 🐛 Troubleshooting

**Can't login?**
- Check username and password
- Verify capslock is off
- Reset credentials in code if needed

**Block list won't save?**
- Check file permissions
- Ensure `blocked_sites.json` exists
- Run with appropriate permissions

**Import failing?**
- Verify JSON format is correct
- Check file path
- Ensure file has read permissions

## 👨‍💻 Developer Info

- **Language:** Python 3
- **Database:** JSON
- **Encryption:** SHA256
- **License:** Open Source

## 📞 Support

For issues or questions:
- Create an issue on GitHub
- Check existing documentation
- Review security logs for errors

## 🌍 Humanitarian Purpose

This tool is designed for:
- Child safety online
- Educational institutions
- Family protection
- Workplace productivity
- Internet safety

## ⚖️ Legal Notice

This tool should only be used for legitimate purposes:
- Protecting minors
- Educational settings
- Workplace management
- Personal device protection

Unauthorized blocking of websites for censorship purposes is not supported.

---

**Made with ❤️ for safer internet** 🔐
