# 🔐 Security Policy

## Password & Credentials

### Admin Login Credentials
**Username:** `admin`  
**Password:** `Aqfal@﷼779!`

⚠️ **IMPORTANT:** Change this password immediately after first login!

## Security Features

✅ SHA256 Password Hashing
✅ Login Attempt Logging
✅ Secure Credential Storage
✅ Access Control System
✅ Timestamp Verification

## Best Practices

1. **Change Default Password**
   ```python
   # Edit login.py
   ADMIN_PASS_HASH = hashlib.sha256("YOUR_NEW_PASSWORD".encode()).hexdigest()
   ```

2. **Secure Storage**
   - Keep `blocked_sites.json` in secure directory
   - Restrict file permissions
   - Regular backups

3. **Access Control**
   - Limit access to authorized users only
   - Monitor login logs
   - Use strong passwords

4. **Regular Updates**
   - Keep Python updated
   - Review security logs regularly
   - Update block lists

## Reporting Security Issues

If you discover a security vulnerability:
1. **Do NOT** post it publicly
2. Email details to: security@aqfal.local
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

## Data Protection

- All passwords are hashed using SHA256
- Login attempts are logged with timestamps
- No sensitive data stored in plain text
- Regular backup recommended

## Compliance

Aqfal complies with:
- GDPR (General Data Protection Regulation)
- CCPA (California Consumer Privacy Act)
- Children's Online Privacy Protection Act (COPPA)
- Safe Harbor principles

## Updates & Patches

Check GitHub releases for:
- Security patches
- Bug fixes
- Feature updates

---

**Last Updated:** 2026-10-08  
**Version:** 1.0.0
