#!/usr/bin/python3
###########################################################################################
# This is a Hacker Story Generator - 2025 GRC Edition
# Born out of idiots (fake hackers) claiming to be all the cybers and the war stories they sadly told.
# Now updated with modern 2025 security nightmares: AI incidents, supply chain disasters,
# OAuth mishaps, leaked API keys, and the eternal struggle of secrets in production.
# Hopefully the legit hackers (and GRC professionals) get some enjoyment from this...
# Author: ED-209-Mk7 (Updated for 2025)
# Setting: Too much caffeine, multiple incident response calls, and existential dread
# Usage: ./hacker_stories.py or $ python3 ./hacker_stories
#############################################################################################

#import the random module
import random
print("\n----------------------===Security Proverbs: 2025===--------------------- \n"
"........Ancient wisdom from the land of DevSecOps........ \n \n")

#security proverbs - sin and consequence pairs
def proverb():
    proverbs=random.choice([
    ("Dev who commit .env to GitHub,", "wake up on HackerNews."),
    ("Admin who set CORS to *,", "find API called from Russia."),
    ("Engineer who hardcode API key,", "find key in GitHub secret scanner."),
    ("Team who deploy on Friday,", "spend weekend in war room."),
    ("Intern who push to main,", "find resume on job board."),
    ("Architect who disable auth 'temporarily',", "find auth still off 3 years later."),
    ("SRE who chmod 777,", "find crypto miner in morning."),
    ("DevOps who set password to 'password123',", "get password sprayed by script kiddie."),
    ("Manager who skip security review,", "get invited to all-hands about 'the incident'."),
    ("Developer who trust npm package published yesterday,", "find backdoor in dependencies."),
    ("Contractor who comment out SSL verification,", "find traffic on Wireshark screenshot."),
    ("Lead who say 'we'll fix it later',", "find 'later' on pen test report."),
    ("Engineer who store secrets in ConfigMap,", "find secrets in kubectl get."),
    ("Team who run containers as root,", "find container escape exploit."),
    ("Admin who expose K8s dashboard to internet,", "find dashboard on Shodan."),
    ("Dev who commit 'removing sensitive data',", "find sensitive data in commit history."),
    ("Startup who move fast and break things,", "find things broken in production."),
    ("Company who set S3 bucket to public,", "find bucket in security researcher tweet."),
    ("Engineer who log credentials at INFO level,", "find credentials in CloudWatch."),
    ("Team who use admin:admin in prod,", "find attacker use admin:admin too."),
    ("Developer who copy-paste from Stack Overflow,", "find SQL injection in code review."),
    ("Manager who say 'security is not priority',", "find security incident is priority."),
    ("Architect who build microservices without auth,", "find lateral movement in audit log."),
    ("DevOps who put secrets in Docker image,", "find secrets in Docker Hub."),
    ("Engineer who disable firewall 'for testing',", "find port scan from China."),
    ("Team who trust the vendor,", "find vendor in breach headlines."),
    ("Admin who click 'URGENT: Click Here',", "get phished, lose MFA seed."),
    ("Developer who name bucket 'prod-secrets',", "find bucket guessed by attacker."),
    ("SRE who turn off monitoring to save cost,", "find incident with no logs."),
    ("Engineer who set JWT expiry to 10 years,", "find token still valid after breach."),
    ("Team who skip dependency updates,", "find Log4Shell in production."),
    ("DevOps who give everyone admin access,", "find junior dev drop production database."),
    ("Developer who test in production,", "find production is down."),
    ("Manager who ignore pen test findings,", "find same findings in breach report."),
    ("Admin who reuse password across systems,", "find credential stuffing attack succeed."),
    ("Engineer who trust user input,", "find XSS in security audit."),
    ("Team who store passwords in plaintext,", "find passwords on Pastebin."),
    ("Developer who disable CSRF protection,", "find bank transfer to Nigeria."),
    ("Architect who build own crypto,", "find crypto broken in academic paper."),
    ("SRE who keep default credentials,", "find Mirai botnet in network."),
    ("Engineer who concatenate SQL queries,", "find Bobby Tables deleted database."),
    ("Manager who rush to production,", "find rollback at 3am."),
    ("Team who ignore security alerts,", "find real breach in spam folder."),
    ("DevOps who trust all certificates,", "find man-in-middle attacker."),
    ("Developer who commit AWS keys,", "find $47,000 Bitcoin mining bill."),
    ("Admin who open port 22 to 0.0.0.0/0,", "find SSH brute force in logs."),
    ("Engineer who parse XML without safety,", "find XXE in vulnerability scan."),
    ("Team who build without rate limiting,", "find DDoS take down service."),
    ("Developer who eval() user input,", "find remote code execution."),
    ("Manager who buy cheapest vendor,", "get what paid for."),
    ("SRE who automate without testing,", "find automation delete everything."),
    ("Engineer who go to sleep with itchy bum,", "wake up with smelly finger."),
    # IT Support / MSP nightmares
    ("IT admin who install Windows 11 auto-update,", "find BitLocker lock out entire company."),
    ("MSP who trust printer drivers,", "spend week troubleshooting PC LOAD LETTER."),
    ("Helpdesk who enable Copilot for users,", "find AI summarize confidential emails to competitors."),
    ("Admin who deploy Recall without consent,", "find screenshots of HR termination notices."),
    ("MSP who patch on Tuesday,", "find Microsoft break printer on Wednesday."),
    ("IT who buy smart coffee maker for office,", "find coffee maker need cloud to brew."),
    ("Company who buy IoT door locks,", "find door locks need internet to unlock."),
    ("Admin who trust HP printer firmware update,", "find printer now require subscription for cyan."),
    ("IT who deploy Windows 11 23H2,", "find Start menu break for entire floor."),
    ("MSP who schedule Teams update,", "find Teams install 47 times in AppData."),
    ("Helpdesk who trust Microsoft 'stable' release,", "find 'stable' break VPN on 10,000 laptops."),
    ("Startup who buy smart bed for office,", "find bed become paperweight when us-east-1 down."),
    ("Company who connect fridge to internet,", "find fridge join botnet, DDoS neighbor."),
    ("IT who buy smart thermostat,", "find thermostat need subscription after 2 years."),
    ("Admin who trust Canon printer,", "find printer demand registry edit to print black."),
    ("MSP who install printer via GPO,", "find printer silently fail, log nothing."),
    ("Helpdesk who trust Bluetooth keyboard,", "find keyboard disconnect during CEO presentation."),
    ("IT who buy smart whiteboard,", "find whiteboard need cloud account to erase."),
    ("Company who trust Cisco wireless,", "find AP need reboot every Tuesday."),
    ("Admin who trust Dell BIOS update,", "find BIOS update brick 200 laptops."),
    ("MSP who trust Microsoft documentation,", "find documentation for Windows 10."),
    ("IT who buy enterprise printer,", "find printer speak PostScript but no English."),
    ("Helpdesk who enable Copilot+ features,", "find NPU mine crypto in background."),
    ("Admin who trust Lenovo firmware,", "find firmware install Superfish 2.0."),
    ("MSP who promise 99.9% uptime,", "spend 0.1% explaining AWS outage."),
    ("IT who connect security cameras to cloud,", "find cameras stream to random IP in China."),
    ("Company who buy smart TV for conference room,", "find TV play ads before every meeting."),
    ("Admin who trust Windows Update quality,", "find update delete user profiles."),
    ("MSP who trust Adobe Acrobat,", "find Acrobat install 12 background services."),
    ("Helpdesk who trust Outlook 365,", "find Outlook cache 40GB on SSD."),
    ("IT who buy IoT light bulbs,", "find light bulbs need firmware update to turn on."),
    ("Company who trust Zoom auto-update,", "find Zoom install web server as root."),
    ("Admin who trust Brother printer,", "find Brother is only one that work, ironically."),
    ("MSP who scripted printer deployment,", "find script work perfectly until it doesn't."),
    ("IT who trust enterprise WiFi,", "find WiFi ask for password after every sleep."),
    ("Helpdesk who tell user 'restart computer',", "find user turn off monitor, call back 'still broken'."),
    ])
    return proverbs
#generate the proverb
def main():
    sin, karma = proverb()
    print(sin,karma,"\n\n")

if __name__ == '__main__':
    main()
