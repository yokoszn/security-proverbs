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

#who commits the sin
def sinner():
    thesinner=random.choice([
    "Dev who commit .env to GitHub,",
    "Admin who set CORS to *,",
    "Engineer who hardcode API key,",
    "Team who deploy on Friday,",
    "Intern who push to main,",
    "Architect who disable auth 'temporarily',",
    "SRE who chmod 777,",
    "DevOps who set password to 'password123',",
    "Manager who skip security review,",
    "Developer who trust npm package published yesterday,",
    "Contractor who comment out SSL verification,",
    "Lead who say 'we'll fix it later',",
    "Engineer who store secrets in ConfigMap,",
    "Team who run containers as root,",
    "Admin who expose K8s dashboard to internet,",
    "Dev who commit 'removing sensitive data',",
    "Startup who move fast and break things,",
    "Company who set S3 bucket to public,",
    "Engineer who log credentials at INFO level,",
    "Team who use admin:admin in prod,",
    "Developer who copy-paste from Stack Overflow,",
    "Manager who say 'security is not priority',",
    "Architect who build microservices without auth,",
    "DevOps who put secrets in Docker image,",
    "Engineer who disable firewall 'for testing',",
    "Team who trust the vendor,",
    "Admin who click 'URGENT: Click Here',",
    "Developer who name bucket 'prod-secrets',",
    ])
    return str(thesinner)

#the karmic consequence
def consequence():
    theconsequence=random.choice([
    "wake up on HackerNews.",
    "find database on Pastebin.",
    "wake up with ransomware note.",
    "find customers on dark web.",
    "get call from CISO at 3am.",
    "wake up to incident response team.",
    "find company on breach notification list.",
    "get visit from compliance team.",
    "wake up with SEC investigation.",
    "find resume on job board.",
    "get featured in security podcast.",
    "wake up to Shodan screenshot.",
    "find credentials in Have I Been Pwned.",
    "get mentioned in CVE.",
    "wake up to pen test report.",
    "find AWS bill for $47,000.",
    "get tagged in security researcher tweet.",
    "wake up to SOC 2 audit failure.",
    "find company logo in breach compilation.",
    "get invited to all-hands about 'the incident'.",
    "wake up with GDPR fine.",
    "find crypto miner in production.",
    "get promoted to VP of Resume Writing.",
    "wake up to empty S3 bucket.",
    "find company in threat intel feed.",
    "get 'let's sync' from CEO.",
    "wake up to ransom note in Comic Sans.",
    "find backdoor older than intern.",
    "get invited to 'talk about culture'.",
    "wake up with smelly finger.",
    "find entire infra on sale in Telegram.",
    "get LinkedIn messages from recruiters.",
    "wake up to 200 Jira tickets.",
    "find production down, backup also down.",
    "get congratulations from threat actors.",
    "wake up to compliance violation.",
    "find logs pointing at own commits.",
    "get mandatory security training invite.",
    "wake up to pentest summary: 'Critical'.",
    "find name in git blame.",
    ])
    return str(theconsequence)
#generate the proverb
def main():
    sin=sinner()
    karma=consequence()
    print(sin,karma,"\n\n")

if __name__ == '__main__':
    main()
