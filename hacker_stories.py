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
    thetarget=random.choice(["the entire customer database embedded in the landing page HTML.",
    "a compromised npm package in production.",
    "leaked API keys in our public GitHub repo;\n (yeah, someone committed .env files again)",
    "the entirety of War & Peace somehow in our Terraform script.",
    "production database credentials in a public Postman collection.",
    "our third-party SaaS vendor's S3 bucket (spoiler: it was set to public).",
    "an LLM that was prompt-injected to return admin credentials.",
    "AWS keys in a meme we posted to Twitter.",
    "production secrets helpfully commented in the React component.",
    "API keys in a Jupyter notebook titled 'PROD_KEYS_DO_NOT_SHARE.ipynb'.",
    "a .git folder exposed on the production website.",
    "the CEO's SSO session token in a screenshot they posted on LinkedIn."])
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
    toolOrVuln=random.choice(["compromised OAuth refresh tokens stored in localStorage",
    "exposed API keys (with a helpful comment: 'TODO: move to env vars')",
    "leaked AWS credentials with a key ID that literally starts with AKIA",
    "an AI chatbot trained on our internal Slack messages",
    "hardcoded JWT secrets set to 'changeme123'",
    "CORS set to allow origin: *",
    "a dependency downloaded 500 million times despite being published yesterday",
    "admin:admin as the default credentials (unchanged since 2019)",
    "an S3 bucket named 'totally-not-production-secrets'",
    "the password 'Password123!' that passed our complexity requirements",
    "a MongoDB instance with no authentication (it's fine, it's behind a firewall)"])
    return str(toolOrVuln)
#what was the exploit; random strings of tech pieces
def exploit():
    verb=random.choice(["to exploit","to abuse","to leverage","to weaponize","to chain together"])
    thevuln=random.choice(["Log4Shell (yes, STILL in 2025).","a supply chain attack (the package was 6 hours old).",
    "stolen OAuth tokens from a phishing email titled 'URGENT: Click Here'.",
    "the .env file someone committed with message 'quick fix'.",
    "an AI model that memorized everyone's SSNs from training data.",
    "the S3 bucket they found by literally guessing company-name-prod.",
    "a CI/CD pipeline with a secret named 'SUPER_SECRET_DO_NOT_STEAL'.",
    "the npm package 'loadash' instead of 'lodash'.",
    "debug mode left on in production (whoops).",
    "the Kubernetes dashboard exposed to 0.0.0.0/0."])
    return str(verb+" "+thevuln)
#the loot they grabbed...or result... the more ridiculous the better
def loot():
    toolOrVuln=random.choice(["compliance automation","incident response playbooks","vendor risk assessments",
    "policy violation reports","IAM privilege reviews","security posture dashboards",
    "threat intelligence feeds","vulnerability management workflows","CSPM scans"])
    link=random.choice(["Once "+selfref2+" got visibility,","After enabling monitoring,","Post-remediation,"])
    link2=(selfref2+" ran "+toolOrVuln)
    link3=random.choice(["to discover","to uncover","to identify","and found"])
    theLoot=random.choice(["47 more API keys in Slack messages titled '#random'.",
    "customer SSNs in plaintext in the Redis cache.",
    "production secrets in 200+ Docker images tagged 'latest'.",
    "OAuth tokens in a GitHub Gist titled 'temp notes'.",
    "AWS keys with AdministratorAccess in a file called 'test.js'.",
    "API credentials helpfully logged at INFO level.",
    "a database backup from 2019 on an intern's laptop.",
    "the prod database password written on a sticky note in a Zoom screenshot.",
    "private keys in a public Docker Hub image with 500K pulls.",
    "every password ever used stored in an unencrypted S3 bucket.",
    "the entire codebase of a competitor (courtesy of prompt injection).",
    "SSH keys in a file committed with message 'removing sensitive data'."])
    return str(link+" "+link2+" "+link3+" "+theLoot)
#what was the end result
def ending():
    theEnding=random.choice(["Now "+selfref2+"'re updating the incident response runbook (again).",
    "The CISO wants a full report by EOD (he's golfing btw).",
    ""+selfref2.capitalize()+" created 47 Jira tickets and closed the laptop.",
    "Still waiting on legal to approve the disclosure (it's been 6 months).",
    "The vendor said 'not our problem' and pointed to section 47.3 of the SLA.",
    "Another day, another supply chain incident. Time to update the SBOM!",
    ""+selfref2.capitalize()+" blamed it on shadow IT (it was definitely shadow IT).",
    "At least "+selfref2+" have good logs... JK, CloudWatch costs too much so they're off.",
    "The dev who did it left the company 3 years ago.",
    "It's fine, "+selfref2+" rotated the keys. All 10,000 of them. By hand.",
    "Turns out the 'temporary' fix from 2019 was still in prod.",
    "The pen test report said this would happen. Nobody read it."])
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
