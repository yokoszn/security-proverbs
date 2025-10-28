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
print("\n----------------------===Hacker Stories: 2025 Edition===--------------------- \n"
"........Keep the spirit of the lies of the skiddies alive (now with AI)!........ \n"
"..........Because every breach is a supply chain attack now!.......... \n \n")

#select opening
def opener():
     opening=random.choice(["So during our last sprint,","Right after the AI audit,","During the 3am incident call,",
     "Last week during compliance review,","After we failed our SOC 2 audit,","During the vendor risk assessment,",
     "While reviewing production logs at 2am,","After the intern pushed to main,","During the all-hands security review,"])
     return str(opening)

#who was involved
def involved():
    global selfref #the involved variable here is global
    global selfref2
    selfref=random.choice(["I","We"])
    if selfref == "I":
        selfref2="I"
        thewhos=random.choice(["I was"])
    if selfref == "We":
        selfref2="we"
        thewhos=random.choice(["we were","the team was"])
    if selfref == "They":
        selfref2="they"
        thewhos=random.choice(["the DevSecOps team was","the red team was","some AI security researchers were","the threat intel team was",])
    whosverb=random.choice(["investigating","responding to","hunting for","remediating","triaging"])
    whodidit=str(thewhos+" "+whosverb)
    return str(whodidit)

#who was the target
def target():
    thetarget=random.choice(["the entire customer database in the landing page HTML.",
    "a compromised npm package.",
    "API keys in our public GitHub repo.",
    "War & Peace in the Terraform script.",
    "prod creds in a public Postman collection.",
    "the vendor's S3 bucket (set to public).",
    "an LLM prompt-injected for admin creds.",
    "AWS keys in a meme on Twitter.",
    "secrets commented in the React component.",
    "'PROD_KEYS_DO_NOT_SHARE.ipynb'.",
    "exposed .git folder on production.",
    "CEO's SSO token in a LinkedIn screenshot."])
    return str(thetarget)
#what was the vector or tool to the vulnerability
def vector():
    verb=random.choice(["deployed","leveraged","fired up","pivoted to",
    "reached for the trusty","consulted ChatGPT and then used"])
    thevector=random.choice(["GitHub secret scanning alerts","Semgrep rules","our SIEM dashboard",
    "TruffleHog","GitGuardian","dependency scanning","SCA tools","SBOM analysis",
    "container image scanning","policy-as-code","an AI-powered vulnerability scanner"])
    link=random.choice(["so that "+selfref2+" could detect","where "+selfref2+" could find"])
    return str(selfref+" "+verb+" "+thevector+" "+link)
#what was the vulnerability; random string of tech pieces
def vuln():
    toolOrVuln=random.choice(["OAuth tokens in localStorage",
    "API keys (comment: 'TODO: move to env vars')",
    "AWS creds starting with AKIA",
    "AI chatbot trained on internal Slack",
    "JWT secret: 'changeme123'",
    "CORS set to *",
    "a dependency published yesterday with 500M downloads",
    "admin:admin (unchanged since 2019)",
    "bucket named 'totally-not-production-secrets'",
    "password 'Password123!' (passed complexity checks)",
    "MongoDB with no auth (behind firewall though)"])
    return str(toolOrVuln)
#what was the exploit; random strings of tech pieces
def exploit():
    verb=random.choice(["to exploit","to abuse","to leverage","to weaponize","to chain"])
    thevuln=random.choice(["Log4Shell (STILL in 2025).",
    "a supply chain attack (package was 6hrs old).",
    "OAuth tokens from 'URGENT: Click Here' phishing.",
    ".env committed with 'quick fix'.",
    "AI model that memorized SSNs.",
    "S3 bucket guessed as company-name-prod.",
    "secret named 'SUPER_SECRET_DO_NOT_STEAL'.",
    "npm typosquat 'loadash'.",
    "debug mode in prod.",
    "K8s dashboard on 0.0.0.0/0."])
    return str(verb+" "+thevuln)
#the loot they grabbed...or result... the more ridiculous the better
def loot():
    link=random.choice(["After scanning,","Post-remediation,","Eventually,"])
    theLoot=random.choice([selfref2+" found 47 API keys in Slack #random.",
    selfref2+" found SSNs in plaintext Redis.",
    selfref2+" found secrets in 200+ images tagged 'latest'.",
    selfref2+" found OAuth tokens in a Gist 'temp notes'.",
    selfref2+" found AWS AdminAccess in 'test.js'.",
    selfref2+" found creds logged at INFO.",
    selfref2+" found a 2019 DB backup on intern's laptop.",
    selfref2+" found prod password on sticky note in Zoom screenshot.",
    selfref2+" found private keys in Docker Hub (500K pulls).",
    selfref2+" found all passwords in unencrypted S3.",
    selfref2+" found competitor's codebase via prompt injection.",
    selfref2+" found SSH keys in commit 'removing sensitive data'."])
    return str(link+" "+theLoot)
#what was the end result
def ending():
    theEnding=random.choice([
    # Blame game - 28+ variations
    ""+selfref2.capitalize()+" blamed DevOps.",
    ""+selfref2.capitalize()+" blamed the platform team.",
    ""+selfref2.capitalize()+" blamed SRE.",
    ""+selfref2.capitalize()+" blamed the security team.",
    ""+selfref2.capitalize()+" blamed the frontend devs.",
    ""+selfref2.capitalize()+" blamed the backend team.",
    ""+selfref2.capitalize()+" blamed the data engineers.",
    ""+selfref2.capitalize()+" blamed shadow IT.",
    ""+selfref2.capitalize()+" blamed the contractors.",
    ""+selfref2.capitalize()+" blamed the intern.",
    ""+selfref2.capitalize()+" blamed the offshore team.",
    ""+selfref2.capitalize()+" blamed the vendor.",
    ""+selfref2.capitalize()+" blamed the cloud provider.",
    ""+selfref2.capitalize()+" blamed the CI/CD pipeline.",
    ""+selfref2.capitalize()+" blamed infrastructure-as-code.",
    ""+selfref2.capitalize()+" blamed the automation.",
    ""+selfref2.capitalize()+" blamed GitOps.",
    ""+selfref2.capitalize()+" blamed Kubernetes.",
    ""+selfref2.capitalize()+" blamed microservices.",
    ""+selfref2.capitalize()+" blamed serverless.",
    ""+selfref2.capitalize()+" blamed the monolith.",
    ""+selfref2.capitalize()+" blamed technical debt.",
    ""+selfref2.capitalize()+" blamed the sprint deadline.",
    ""+selfref2.capitalize()+" blamed 'move fast and break things' culture.",
    ""+selfref2.capitalize()+" blamed the lack of guardrails.",
    ""+selfref2.capitalize()+" blamed the previous architect.",
    ""+selfref2.capitalize()+" blamed the legacy system.",
    ""+selfref2.capitalize()+" blamed the migration.",
    # Other endings
    "CISO wants report by EOD.",
    "Created 47 Jira tickets.",
    "Legal still reviewing (6 months now).",
    "Vendor: 'Not our problem, see SLA §47.3'.",
    "Dev left company 3 years ago.",
    "Rotated all 10,000 keys by hand.",
    "Temp fix from 2019 still in prod.",
    "Pen test warned this. Nobody read it.",
    "Logs turned off (CloudWatch too expensive).",
    "Updating runbook again.",
    "Another supply chain incident."])
    return str("\n"+theEnding)
#run the story
#set the invlolved variable as global
selfref=""
opening=opener()
involved=involved()
target=target()
vector=vector()
vuln=vuln()
exploit=exploit()
loot=loot()
ending=ending()
def main():
    print(opening,involved,target,"\n"+vector,vuln,exploit,loot,ending,"\n\n")

if __name__ == '__main__':
    main()
