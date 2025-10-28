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
     "Last week during compliance review,","After we failed our SOC 2 audit,","During the vendor risk assessment,"])
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
    thetarget=random.choice(["our AI model training pipeline.","a compromised npm package in production.",
    "leaked API keys in our public GitHub repo;\n (yeah, someone committed .env files again)",
    "OAuth tokens hardcoded in the mobile app.","secrets accidentally logged to CloudWatch.",
    "our third-party SaaS vendor's S3 bucket.","an LLM that was prompt-injected.",
    "a supply chain attack via a Docker base image.","production secrets in a Kubernetes ConfigMap.",
    "API keys in a Jupyter notebook someone uploaded.","our CI/CD pipeline with overly permissive IAM roles."])
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
    toolOrVuln=random.choice(["compromised OAuth refresh tokens","exposed API keys","leaked AWS credentials",
    "an insecure AI model endpoint","hardcoded JWT secrets","misconfigured CORS policies",
    "a poisoned Python package","vulnerable container dependencies","an over-permissioned service account",
    "prompt injection vulnerabilities","a malicious GitHub Action"])
    return str(toolOrVuln)
#what was the exploit; random strings of tech pieces
def exploit():
    verb=random.choice(["to exploit","to abuse","to leverage","to weaponize","to chain together"])
    thevuln=random.choice(["Log4Shell (yes, still in 2025).","a supply chain compromise.",
    "stolen OAuth tokens from a phishing campaign.","exposed credentials from a leaked .env file.",
    "an AI model that leaked PII in its training data.","misconfigured cloud storage with public read access.",
    "a compromised CI/CD pipeline with AWS admin keys.","dependency confusion in our package manager."])
    return str(verb+" "+thevuln)
#the loot they grabbed...or result... the more ridiculous the better
def loot():
    toolOrVuln=random.choice(["compliance automation","incident response playbooks","vendor risk assessments",
    "policy violation reports","IAM privilege reviews","security posture dashboards",
    "threat intelligence feeds","vulnerability management workflows","CSPM scans"])
    link=random.choice(["Once "+selfref2+" got visibility,","After enabling monitoring,","Post-remediation,"])
    link2=(selfref2+" ran "+toolOrVuln)
    link3=random.choice(["to discover","to uncover","to identify","and found"])
    theLoot=random.choice(["47 more API keys in Slack messages.","customer PII in AI training datasets.",
    "production secrets in 200+ Docker images.","OAuth tokens in browser localStorage.",
    "AWS keys with AdministratorAccess in a Lambda function.","API credentials in application logs.",
    "SSO bypass vulnerabilities.","22 critical CVEs in production containers.","unencrypted backups with customer data."])
    return str(link+" "+link2+" "+link3+" "+theLoot)
#what was the end result
def ending():
    theEnding=random.choice(["Now "+selfref2+"'re updating the incident response runbook.",
    "The CISO wants a full report by EOD.",
    ""+selfref2.capitalize()+" created 47 Jira tickets and called it a day.",
    "Still waiting on legal and compliance to approve the disclosure.",
    "The vendor swears it's not their fault.",
    "Another day, another supply chain incident.",
    ""+selfref2.capitalize()+" blamed it on shadow IT.",
    "At least "+selfref2+" have good logs... oh wait, the retention policy expired.",
    "The AI security team is now reviewing all LLM prompts."])
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
