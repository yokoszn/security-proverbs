# Security Proverbs: 2025 Edition

Ancient wisdom from the land of DevSecOps, IT support, and MSP hell.

A Python script that generates haiku-style security proverbs in the format of "man who go to sleep with itchy bum, wake up with smelly finger" - but for 2025 cybersecurity, cloud disasters, and IT support nightmares.

Perfect for Message of the Day (MOTD) in CLI/TUI applications, GRC tools, security dashboards, or anywhere you need a daily reminder of the beautiful chaos we're all living through.

## Examples

```
Dev who commit .env to GitHub, wake up on HackerNews.

MSP who patch on Tuesday, find Microsoft break printer on Wednesday.

Startup who buy smart bed for office, find bed become paperweight when us-east-1 down.

Admin who trust Canon printer, find printer demand registry edit to print black.

Team who deploy on Friday, spend weekend in war room.

Engineer who concatenate SQL queries, find Bobby Tables deleted database.

Helpdesk who tell user 'restart computer', find user turn off monitor, call back 'still broken'.
```

## Features

**100+ Security & IT Proverbs covering:**
- Modern cloud security disasters (API keys in GitHub, secrets in prod, OAuth nightmares)
- Supply chain attacks and dependency hell
- AI/LLM security incidents (prompt injection, data leakage)
- Windows 11 chaos (BitLocker lockouts, broken updates, profile deletion)
- Printer hell (all brands, all problems)
- IoT cloud dependency disasters (smart devices becoming paperweights)
- MSP/IT support classics (Teams installing 47 times, users turning off monitors)
- Classic security mistakes with karmic consequences

Each proverb pairs a security sin with its logical consequence - no random nonsense, just painful truth.

## Usage

### Basic Usage
```bash
python3 hacker_stories.py
```

### MOTD in CLI/TUI Applications

**Linux/Unix MOTD:**
```bash
# Add to /etc/profile.d/security-proverb.sh
python3 /path/to/hacker_stories.py

# Or add to ~/.bashrc, ~/.zshrc
python3 ~/hackerstories/hacker_stories.py
```

**SSH MOTD:**
```bash
# Add to /etc/ssh/sshd_config
# Then create /etc/motd script
echo '#!/bin/bash' > /etc/motd
echo 'python3 /path/to/hacker_stories.py' >> /etc/motd
chmod +x /etc/motd
```

**In Your Python CLI/TUI App:**
```python
import subprocess
import random

def show_security_proverb():
    """Display a random security proverb on app startup"""
    try:
        result = subprocess.run(['python3', 'hacker_stories.py'],
                              capture_output=True, text=True)
        print(result.stdout)
    except:
        pass

# Call on app startup
if __name__ == '__main__':
    show_security_proverb()
    # ... rest of your app
```

**As a Module:**
```python
# Import the proverb function directly
import sys
sys.path.append('/path/to/hackerstories')
from hacker_stories import proverb

sin, karma = proverb()
print(f"{sin} {karma}")
```

## Use Cases

- **GRC Tools**: Remind compliance teams of daily security chaos
- **Security Dashboards**: Add levity to your SIEM
- **DevOps/SRE Tools**: Daily reminder of what not to do
- **IT Helpdesk Systems**: Solidarity through shared pain
- **SSH/Terminal MOTD**: Greet sysadmins with wisdom
- **Slack/Discord Bots**: Daily security proverb channel
- **CI/CD Pipelines**: Warning message before deployment

## Categories

**DevSecOps & Cloud:**
- Secrets management disasters
- Cloud misconfigurations
- CI/CD security fails
- Container & K8s nightmares

**IT Support & MSP:**
- Windows 11 update chaos
- Printer problems (all of them)
- Microsoft product quirks
- User support classics

**IoT & Cloud Dependency:**
- Smart devices needing cloud to function
- AWS region outages bricking hardware
- Subscription-based basic functionality

**Classic Security:**
- SQL injection
- XSS and CSRF
- Phishing and social engineering
- Weak passwords and auth

## Contributing

Got a good sin-consequence pair? PRs welcome! Follow the format:
```python
("Person who do foolish thing,", "suffer appropriate consequence.")
```

Make sure the consequence logically follows from the sin - we're going for dark humor based on painful truth, not random chaos.

## License

Use it, abuse it, put it in your MOTD. Just don't blame us when users realize how accurate these are.
