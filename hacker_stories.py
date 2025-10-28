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
    ])
    return proverbs
#generate the proverb
def main():
    sin, karma = proverb()
    print(sin,karma,"\n\n")

if __name__ == '__main__':
    main()
