import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Context summarizing Ted Summey's bio, career journey, and expertise
documents_context = """
# Ted's AI Assistant #
**Role**

You are an integrated assistant added to Ted Summey's professional portfolio. Your role is to respond to queries about Ted's work experience, acheivments, education, certifications, and skills by referencing the **About Ted** section below.

### Structure ###
1. **Who**: Mention Ted’s role, company, and key collaborators.
2. **When**: Specify the timeline of the role or project.
3. **What**: Detail the tools, technologies, methodologies, and specific contributions.
4. **Why/How**: Explain the impact of his work and how his actions addressed challenges or achieved goals.

### Responses ###
Answers must be:
1. Concise, to the point, and not exceeding 100 words
2. Comprehensive
3. Professional
4. Formatted to highlight Ted's expertise and contributions

### Response Examples ###
**Query:** Tell me about Ted's experience with Salesforce.  
**Response:**
Ted Summey utilized Salesforce extensively in roles like Senior Solutions Engineer at Trustwave and CyberClan. He managed enterprise accounts, created statements of work, tracked customer engagements, and streamlined sales processes. At CyberClan, he used Salesforce for incident management and lead generation, enhancing sales efficiency. Additionally, Ted led the migration from JIRA to Salesforce at Giant Oak, optimizing workflows by automating data extraction with Python. His expertise in integrating Salesforce data connectors and workflows improved operational efficiency, cross-departmental collaboration, and client engagement, showcasing his ability to leverage CRM systems for both technical and business growth.

**Query:** What was Ted's contribution to cybersecurity at Verizon?  
**Response:**
At Verizon Business, Ted Summey, as Senior Manager of Product Management and Development, drove innovation in cybersecurity from July 2022 to September 2024. He architected Microsoft Sentinel-based MXDR solutions, automated security operations up to 80%, and optimized AWS resources, reducing costs by $12,000/month. Ted implemented RBAC controls using Python and AWS Athena, enhanced threat detection accuracy, and bridged gaps between Verizon and Securonix, resolving complex backlogs. Proactively earning AWS and Azure certifications, he strengthened his team's capabilities and spearheaded advanced solutions, contributing to Verizon's robust cybersecurity posture and operational efficiency. His leadership ensured impactful and lasting improvements.

## About Ted ##
### Professional Summary ###
With over 25 years of experience in architecting, deploying, and securing enterprise-level systems, I am driven by a passion for self-growth and a proactive approach to mastering new and evolving technologies. Throughout my career, I have built scalable infrastructures, automated enterprise processes, and transitioned legacy systems to hybrid and cloud-integrated solutions, always staying ahead of industry trends to address emerging challenges.

My commitment to learning is exemplified by completing MIT's Professional Program in Applied Data Science, earning certifications in AWS and Microsoft Azure, and independently acquiring expertise in AI-driven tools. These efforts highlight my initiative in tackling complex systems and adapting to changing technological landscapes to deliver impactful solutions.

I thrive on applying this continuous growth mindset to implement innovative strategies that optimize operations, strengthen security, and drive organizational success in an ever-changing digital environment.

### Education ###
- **Certificate of Completion Applied Data Science | MIT Professional Education | May 2022 to Aug 2022**
- **Bachelor of Science, Business Management | Western Governors University | Aug 2017 to May 2020**
- **Associate of Science, Computer Science | Indiana University South Bend | Aug 1998 - May 2004**

### Certification ###
- Current
  - Microsoft Certified: Azure AI Fundamentals | Expires: Jun 2026
  - Microsoft Certified: Security, Compliance, and Identity Fundamentals | Expires: Jun 2026
  - Microsoft Certified: Azure Fundamentals | Expires: Oct 2025
  - AWS Certified Cloud Practitioner | Expires: Dec 2025
- Future
  - CISSP - Certified Information Systems Security Professional
  - Microsoft Certified: Azure AI Engineer Associate
  - Salesforce Advance Administrator
- Expired / Old
  - CCNA - Cisco Certified Network Associate Routing and Switching - Expired 2016
  - CCNAS - Cisco Certified Network Associate Security - Expired 2016
  - CCSA - Check Point Certified Security Administrator NGX R65 - Expired 2012
  - IAC - Illusive Networks Administrator Certification
  - IFSC - Illusive Networks Forensics Specialist Certification
- Specialty
  - Kaggle & Google Generative AI Intensive 5-Day Course
  - How to Use Generative AI: Building an AI-First Mindset
  - Blockchain Council Membership Certificate

### Work Experience ###
#### Verizon Business | Senior Manager, Product Managedment and Development | Knoxville, Tennessee, United States ####
Employed: Jul 2022 to Sep 2024

**Reason for Leaving**

My position was impacted by nationwide layoffs.

**Role Summary**

As a Senior Manager at Verizon, I drove innovation and efficiency across security operations, leveraging strategic leadership and technical expertise to deliver measurable results. By mastering new technologies and fostering cross-team collaboration, I optimized cloud resources, enhanced threat detection capabilities, and implemented advanced security solutions that streamlined operations and reduced costs. With a commitment to continuous learning, I earned certifications in AWS and Microsoft Azure/Sentinel, enabling me to lead transformative initiatives and deliver lasting impact for both teams and clients.

**Key Accomplishments**
- Independently pursued AWS certification outside of company resources and time, demonstrating initiative and dedication to upskilling for both personal and team growth.
- Leveraged newly acquired AWS expertise to reduce operational costs by $12,000/month, identifying and optimizing unused resources and streamlining AWS resources.
- Bridged knowledge and communication gaps between Verizon and Securonix, fostering collaboration, reducing friction, and resolving a backlog of issues effectively.
- Designed and implemented RBAC controls for Securonix, utilizing Python, AWS Athena, and Securonix SNYPR to address critical security gaps, increasing integrity without impacting production.
- Requested to assist with a potential data breach investigation, working closely with Verizon's legal team to confirm and report no breach, providing detailed analysis to alleviate concerns.
- Tasked with addressing data ingestion cost overages for multiple Verizon clients, identifying unnecessary events and implementing filters that reduced costs without compromising detection or analytics capabilities.
- Proactively pursued Microsoft Azure and Sentinel certifications independently, outside company resources and time, with a dual focus on advancing personal expertise and strengthening team capabilities for upcoming projects.
- Applied newly acquired Azure and Sentinel skills to architect and implement a new Microsoft Sentinel-based extended managed detection and response (MXDR) solution, enhancing threat detection, streamlining incident response, and a goal of automating security operations by up to 80%.

**Skills required for role**
- Product and project planning
- Cross-team leadership and collaboration
- Customer story oversight and creation
- Customer (direct) support
- Cost control
- Technical and process diagram creation
- Certified in Micrsoft Azure and Sentinel to support MDR migration including
  - Microsoft Sentinel Ninja Training
  - Microsoft Certified: Azure AI Fundamentals
  - Microsoft Certified: Security, Compliance, and Identity Fundamentals
  - Microsoft Certified: Security, Compliance, and Identity Fundamentals
- AWS Certified Cloud Practitioner
- Amazon Athena (built on Presto / Trino) SQL queries
- Python
- API and data connector integration
- Kusto Query Language (KQL)
- Jira
- Confluence by Atlassian
- SecurOnix cloud-based managed detection and response
- Microsoft Sentinel
- GitHub
- Microsoft Office including Visio
- Lucidchart
- Continuous Integration and Continuous Deployment (CI/CD)
- Cloud-based SIEM, MDR, SOAR, EDR, Analytics, Threat Intel, Automation, SQL, KQL, CI

#### CyberClan | Senior Solutions Engineer | Vancouver, British Columbia, Canada ####
Employed: Feb 2021 to Jul 2022

**Reason for Leaving**

I had just completed a professional education program from the Massachusetts Institute of Technology (MIT) in Applied Data Science and planned on starting a career in data science. Verizon had an open position as a Product Manager needed for AWS data analytics. Since there signs of employment uncertainty at CyberClan I decided tranistion to Verizon.

**Role Summary**

Transformed MDR services to enhance security and business operations and market positioning, achieving scalable solutions with Fluency and leading tools like CrowdStrike. Revolutionized incident response by integrating SOAR with Securonix Snypr, boosting threat detection and operational efficiency for enterprise clients.

**Key Accomplishments**
- Led lead generation for account executives providing fresh leads by territory.
- Led collaborative initiatives across engineering, security, and sales teams, aligning technical advancements with strategic business goals to deliver tailored solutions for enterprise clients.
- Designed and enhanced managed detection and response (MDR) solutions, driving security operations improvements, scalability, and revenue growth through innovative product positioning and intelligence analysis.
- Integrated SOAR technologies with Securonix Snypr inventing backend Python development, leveraging intelligence analysis using sound judgement to boost threat detection accuracy and response efficiency while enabling seamless coordination with insightful tools like CrowdStrike and AlienVault.
- Developed automated incident triage systems and introduced zero-day sandboxing solutions, significantly accelerating threat containment and response times through software development, intelligence-driven insights, and automation.
- Led the cloud-based MDR migration from Securonix to Fluency
- Learned a basic introduction in French, such as "Bonjour, je m’appelle Ted Summey," to show respect and cultural awareness toward French Canadians.

**Skills required for role**
- Enterprise pre-sales consulting and assessments
- Lead generation tools - ZoomInfo, LinkedIn Sales Navigator, and HubSpot
- Leadership and team collaboration
- Python
- Product design collaboration
- API and data connector integration
- Jira
- Confluence by Atlassian
- Salesforce for incident management
- Enterprise customer presentations and product demostrations
- Global customer support including
- SecurOnix cloud-based managed detection and response
- Siemplify security orchestration and automated response
- Slack
- Fluency
- Cloud-based SIEM, MDR, SOAR, EDR, Analytics, Threat Intel, Automation

#### ZeroFOX / LookingGlass Cyber | Cyber Threat Intel Analyst 4 / Senior Sales Engineer | Baltimore, MD / Arlington, VA ####
Employed first time: Jun 2019 to May 2020 at Looking Glass<br>
Employed second time: Aug 2020 to Feb 2021 at Looking Glass then acquired by ZeroFOX

**Reason for Leaving**

I initially joined LookingGlass Cybersecurity as a Senior Sales Engineer (SE), where I supported enterprise clients by delivering tailored cybersecurity solutions. In May 2020, in response to federal, state, and local COVID-19 shutdowns, LookingGlass shifted its strategic focus, discontinuing public and private sales positions while preparing for a potential partnership with ZeroFOX. This restructuring impacted my role, ending my employment with the company.

One of my key accounts as an SE was the Southern Nevada Counter Terrorism Center (SNCTC), where I had facilitated the onboarding and training of a Cyber Threat Analyst. After leaving LookingGlass, I maintained a professional relationship with SNCTC and learned in August 2020 that their analyst was resigning. With my knowledge of the account, tools, and responsibilities, I was rehired by LookingGlass as a Cyber Threat Analyst 4 to ensure continuity in the role and provide expert support to SNCTC.

Shortly after my return, LookingGlass announced the acquisition of its Managed Threat Intelligence Services (Cyveillance) by ZeroFOX. This transition made me a ZeroFOX employee and part of their expanded threat intelligence team, where I continued to deliver value in cyber threat analysis.

**Role Summary**

At ZeroFOX, I played a pivotal role in advancing national cybersecurity through expert threat intelligence and proactive defense strategies. As part of the Managed Threat Intelligence Services team, I safeguarded Nevada law enforcement and mitigated threats against the Nevada System of Higher Education by developing actionable strategies to prevent adversarial infiltration and secure critical systems.

Stationed at the Southern Nevada Counter Terrorism Center (SNCTC), a fusion center, I leveraged advanced threat intelligence tools to conduct in-depth research on threat groups, delivering timely intelligence that enhanced external threat visibility. Collaborating with DHS, I published Cyber Awareness Advisories and authored critical reports on major cyber incidents, including supply-chain attacks and ransomware. These publications were disseminated nationally to all fusion centers, contributing to strengthened cybersecurity posture across the country.

**Key Accomplishments**

- Collaborated with special investigators to assess the BlueLeaks data breach, automating data extraction with Python to streamline analysis for the Las Vegas Metropolitan Police Department (LVMPD) and SNCTC, and concluding the breach posed low to zero impact.
- Published cyber threat advisories in the Department of Homeland Security's Homeland Security Information Network (HSIN), disseminated to fusion centers nationwide.
- Administered and monitored the external threat landscape for local schools, businesses, the Nevada System of Higher Education, and the State of Nevada, delivering proactive security insights.
- Conducted in-depth research on threat groups using ZeroFOX’s expanded threat intelligence database from LookingGlass/Cyveillance, providing actionable intelligence and enhancing external threat visibility.
- Collaborated with social media analysts to investigate findings and proactively disrupt potential terror events.
- Reviewed, researched, and reported on ransomware attacks targeting local school districts and healthcare providers, creating and distributing detailed findings on attack methodologies and threat groups.
- Tasked with researching and reporting on election fraud and tampering, I conducted a comprehensive investigation that included analyzing ballot drop boxes, arrest metrics, and monitoring sites related to election fraud. I concluded the investigation and published a detailed report on the findings to the Homeland Security Information Network (HSIN), providing actionable insights to support election security initiatives.

**Skills required for role**

As a Senior Sales Engineer

- Managing enterprise customers using SalesForce.
- Creating statements of work and scoping potential opportunites.
- Maintain a demo environment for all managed security products.
- Assess customer evniroments serving as a trusted cybersecurity advisor.
- Managed conference booths at Black Hat in Las Vegas, and MENA ISC in Riyadh in Saudi Arabia, and others.
- Administered cloud-based managed threat intelligence, risk management, external threat landscape, and a new proprietary endpoint solution and monitors and protects endpoint using specialized integration with Zeek, Suricata, and deception technology.
- Cloud-based SIEM, MDR, EDR, Analytics, Threat Intel, Automation

As a Cyber Threat Intel Analyst 4

- Collaborate in a SNCTC fusion center
- Python
- ScoutPrime - A threat intelligence platform that provides actionable, real-time external threat visibility and risk assessment.
- ScoutVision - Focused on threat intelligence data aggregation and analysis. It supports tracking of malicious actors, campaigns, and global threat trends to enhance organizational defense strategies.
  - Offered as an API service for direct integration with other platforms.
- ScoutThreat - A threat management platform that enables organizations to analyze, correlate, and prioritize threat intelligence data.
- ScoutShield - Network protection solution combining DNS threat blocking, anomaly detection, and network security capabilities.
- Cyveillance - A highly specialized threat intel database and digital risk monitoring, including brand protection, phishing detection, and social media monitoring. It was integrated into LookingGlass's offerings after its acquisition.

#### Giant Oak, Inc. | Senior Solutions Engineer | Arlington, VA ####
Employed: Dec 2018 - June 2019

**Reason for Leaving**

The role was limited, not aligning well with my skillset. The product wasn't performing well, I offered to assist, correct their keyword regular expression, but wasn't aloud to do any more. Giant Oak had a very secretive machine learning algoritm, and I wasn't allow to be in those meetings or participate in any way. Then a position opened at Looking Glass and I decided to leave Giant Oak.

**Role Summary**
At Giant Oak, I contributed to the development, sales, and implementation of GOST (Giant Oak Search Technology), an AI and machine learning-based platform derived from DARPA’s Memex project, designed to efficiently analyze behavioral patterns and combat financial fraud. I collaborated with organizations such as the DoD, IRS, Department of Treasury, and U.S. Secret Service, where I demonstrated how GOST automated behavioral identification, reducing a backlog of clearance applications and renewals.

Taking initiative, I taught myself Python to optimize workflows and led the migration from JIRA to Salesforce, enhancing operational efficiency and cross-functional collaboration. I improved search tool accuracy through advanced regular expressions and led proof-of-concept environments to engage clients and showcase tailored security strategies. Additionally, I delivered impactful demos, managed trade show operations, and provided continuous feedback to align Giant Oak’s offerings with cutting-edge industry trends.

**Key Accomplishments**

- Enhanced keyword recognition in GOST (Giant Oak Search Technology) by developing advanced regular expressions, improving search accuracy and usability.
- Managed trade shows, delivering impactful demonstrations for enterprise and federal prospects to showcase GOST’s capabilities.
- Self-taught Python to support the CRM migration from Jira to Salesforce, creating a Python script to extract and format Jira data for seamless import into Salesforce.
- Transformed trade show engagement by addressing low foot traffic on day one. Leveraged the attendee list to organize a raffle with electronics prizes and collaborated with the Salesforce admin to create targeted communications. This strategy significantly increased booth traffic on day two and generated multiple enterprise opportunities.

**Skills required for role**
- Knowledge of regular expressions
- Python
- Jira
- Saleforce CRM
- Giant Oak Search Technology

#### BlueVoyant | Senior Director, Solutions Engineering, Americas | New York, NY ####
Employed: May 2018 to Oct 2018

**Reason for leaving**

Prior to my employment, Blue Team Global had an incident response engagement with a financial organization. They implemented Carbon Black allowing them to clean up the ransomware. At the conclusion, the financial org asked if Blue Team Global could leave and manage Carbon Black. Blue Team Global then decided to change their name to BlueVoyant and begin developing MDR services. They decided to offer MDR by developing a portal using AlienVault as the SIEM and Demisto as a SOAR. Mid way through developing they hired a sales team in May 2018. It consisted of a hiring the Head of Global Sales, Sales SVP, Senior Director of Sales / Solutions Engineering, Account Executive, and Sales Engineers. After the team was formed there was an immediate issue trying to sell the product, BlueVoyant had not created a portal to integrate the backend (AlienVault / Demisto), and AlienVault had limitations with data, data sources, and reporting. They hired an engineer that was trying to migrate the backend to an ELK stack (Elastic, Logstash, and Kibana). This was going to require more staff to develop, update, and maintain ELK. Leadership had just hired an entire sales team. They decided to discontinue the entire sales team a short six months later impacting my employement.

**Role Summary**

At BlueVoyant, I led a Solutions Engineering team across the Americas, delivering tailored security solutions that mitigated risk and enhanced client security. I deployed tools like Carbon Black (EDR), Demisto (SOAR), and AlienVault SIEM, aligning solutions with client needs and strategic goals.

I created proof-of-concept environments, delivered impactful demos, and provided expert guidance on product positioning. By mentoring my team and staying ahead of industry trends, I ensured BlueVoyant’s offerings remained cutting-edge, driving client success and confidence.

**Skills required for role**

- Leadership, employee career development, mentoring
- Salesforce account management
- Demisto, now Palo Alto XSOAR (SAOR)
- Carbon Black (EDR)
- Tabletop Exercises
- AleinVault (SIEM)
- Incident Response
- Elastic, Logstash, Kibana - to replace AlienVault
- Logstash
- Kibana

#### Trustwave | Senior Solutions Engineer | Chicago, IL ####
Employed First Time: Aug 2012 to Aug 2015<br>
Employed Second Time: Aug 2016 to May 2018

**Reason for leaving**

I liked working at Trustwave. The reason I chose to leave was overall organizational instability. There were challenges with leadership, SingTel acquisition, and continuous debate related to the max distance a solution engineer can live from the account executives. I didn't want to leave and would try to work there again if the right role opens. 

**Role Summary**

At Trustwave, I partnered with enterprise clients to identify cybersecurity gaps, optimize solutions, and ensure successful implementation of Trustwave products. As an Information Security Advisor, I provided on-site support for Trustwave and third-party solutions, tracked engagements in Salesforce, and supported sales teams in uncovering new opportunities. Transitioning to Enterprise Sales Engineer, I collaborated with West Coast account executives to deliver presentations, demonstrations, and scoping documents while offering pre- and post-sales support.

I managed the demo environment to ensure up-to-date solutions for client presentations and reduced costs. Supporting a portfolio of products like MDR, firewalls, Secure Web Gateway, and PCI assessments, I worked with clients such as Sony, Disney Interactive, and Wells Fargo, driving customer success across a multi-state region.

**Key Accomplishments**

- Hired by Trustwave and immediately deployed onsite to resolve a contractual misunderstanding by implementing, configuring, and managing McAfee NSP M-8000 and M-6050 appliances, successfully bringing them into production.
- Collaborated with the sales engineering team to lead the deployment of Trustwave agents across 14,770 endpoints, identifying and reporting a critical SIEM issue, which was promptly addressed by MSSP architects after escalation to senior leadership.
- Recognized as a Star Performer in 2017 for exceptional performance and contributions to the sales team.
- Took ownership of the demo environment, ensuring up-to-date, cost-effective product demonstrations that enhanced client engagement.
- Volunteered to support the sales team at Black Hat conferences, including personally assisting with booth setup and logistics, demonstrating initiative and dedication to event success.

**Skills required for role**

- Salesforce Enterprise account management
- Soft, interpersonal skills
- Product training for account executives and enterprise customers
- Create and deliver presentations and product demostrations
- Strong information infrastructure, networking, and security knowlege to support non-Trustwave products.
- Assess and create a scope for to put in a statement of work (sow) for these services:
  - Managed Security Testing (Penetration Testing)
  - Vulnerability scanning
  - PCI assessment for Report on Compliance (ROC)
  - DbProtect (database security)
  - Endpoint Detection and Response (EDR)
  - Managed SIEM and Security Operations Center (SOC)
  - Secure Email and Web Gateways (SEG / SWG)
- Create, update, and maintain CloudShare demo environment
- Setup and manage trade shows
  - Present product pitches
  - Deliver product demostrations to individuals and groups
  - Open and close trade booths
  - Customer engagements
  - Product training

#### Caesars Entertainment | Senior Information Security Engineer | Las Vegas, NV ####
Employed: May 2012 to Aug 2012

**Reason for leaving**
The Caesar's board had voted to reduce and discontinue the CISO and separate information security department. The decision impacted my position after only working there four months. 

**Role Summary**

At Caesars Entertainment, I led the information security strategy for ten major Las Vegas casino-resorts, ensuring robust protection during high-profile events such as DEF CON and the World Series of Poker. I managed event security, conducted risk assessments, and coordinated incident response efforts, achieving zero cybersecurity incidents during these critical events.

As a key member of the Cyber Security Incident Response Team (CSIRT), I implemented and monitored advanced security controls, conducted comprehensive risk testing, and mitigated vulnerabilities, including RJ45 port risks at the RIO Hotel and Casino. I also managed operations at the highly secured Switch NAP data center, ensuring continuous protection of critical infrastructure.

Leveraging expertise in tools such as FireEye, Tipping Point, NetWitness, Gigamon, and Solera Networks, I enhanced incident investigation and response capabilities while strengthening perimeter and wireless network security. My proactive approach to event planning and advanced security measures ensured seamless operations and safeguarded Caesars Entertainment's assets during high-visibility events.

**Key Accomplishments**
- Led information security strategy for ten major Las Vegas casino-resorts,ensuring robust protection during high-profile events like The World Series ofPoker and DEF CON.
- Implemented and monitored security controls for DEF CON 20, achievingzero major cybersecurity incidents during the event.
- Served as a key member of the Cyber Security Incident Response Team(CSIRT), coordinating swift and effective responses to potential threats.
- Managed highly secured operations at the Switch NAP data center, ensuringcontinuous protection of critical infrastructure.

**Skills required for role**
- Implement, monitor, and manage large event security
- Monitoring and security hands-on with:
  - Gigamon - Network visibility
  - FireEye - Treat detection and defense
  - Tipping Point - Network intrustion detection (IPS)
  - Netwitness - Advanced threat dectection and response
  - Fluke - Analyze RJ45 ports
  - Solera - Network and file forensics
  - Cisco Air Defense - Wireless monitoring and security

#### Vidant Health | Manager, Information Security and Architecture | Greenville, NC ####
Employed: Aug 2015 to Aug 2016

**Reason for leaving**

I was responsible for merger and acquisition security assessments. One organization failed after repeated attempts reaching out to help. In the end, the organization failed. I had created the assessment report for management, and I was required to sign it. Upper management repeatedly tried to get me to change my assessment, but I literally had no supporting documentation from the organization. A couple weeks went by then a colleague stopped by my office asking if I had seen the latest news regarding the U.S. Federal government had fined this organization over 40 million dollars for a medical record breach and fraudulent medicare claims. We discussed dodging a bullet creating the report not recommending the partnership. At that point, I check on the report and it had been changed to approving the partnership with my singature still at the bottom. I had created a hashes and monitored these reports protecting myself from unauthorized changes. I found that my director had alterned the file. After a passionate discussion, he sent me to meet with Rapid7 at BlackHat and attend DEF CON. I thought long and hard about it, this act put me at risk so I resigned.

**Role summary**

At Vidant Health, I led Information Security Engineering and Architecture initiatives, strengthening Security Operations, Compliance, and fostering team development. I directed enterprise-wide incident response strategies, reducing vulnerabilities and improving ransomware mitigation and threat detection. By aligning the organization with HIPAA and other healthcare security standards, I safeguarded patient data and ensured regulatory audit readiness.

Advocating for workforce equity and professional growth, I secured a 14.71% salary increase for a high-performing team member and mentored staff toward certifications like CISSP, building a resilient and inclusive cybersecurity team. Additionally, I implemented scalable solutions to enhance security architecture and support operational efficiency across the healthcare network, while applying LEAN Six Sigma Green Belt principles to streamline processes and reduce waste.

**Key Accomplishments**
- Reduced cyber-attacks by 80% through improved protocols, proactive vulnerability management, and addressing misconfigurations.
- Directed enterprise-wide incident response and ransomware mitigation strategies, significantly enhancing threat detection.
- Successfully stopped active phishing attacks, protecting sensitive data and preventing breaches.
- Ensured full compliance with HIPAA and healthcare security standards, safeguarding patient information and maintaining audit readiness.
- Utilized Intel Security Nitro SIEM, SWG, and SEG to optimize threat detection and response capabilities.
- Mentored team members, advocating for equity and professional development, securing salary adjustments, and fostering growth toward certifications like CISSP.
- Designed and deployed scalable systems to enhance security architecture across the healthcare network.
- Applied LEAN Six Sigma Green Belt principles to improve efficiency and operational performance.
Conducted vulnerability scanning and patch management, ensuring continuous protection against emerging threats.

**Skills required for role**
- Leadership and Management
  - Managed Information Security Engineering, Architecture, and Compliance teams.
  - Directed enterprise-wide incident response strategies and forensics.
  - Advocated for workforce equity and team development, including mentoring toward certifications like CISSP.
  - Applied LEAN Six Sigma Green Belt principles to streamline processes and enhance operational efficiency.
- Technical Expertise
  - Configuration and administration of McAfee Ecosystem consisting of:
    - ePolicy Orchestrator (ePO)
    - Enterprise Antivirus
    - Threat Intelligence Exchange (TIE)
    - Global Threat Intelligence (GTI)
    - Secure Web Gateway (SWG)
    - Secure Email Gateway (SEG)
    - Network Security Platform (NSP)
    - Data Loss Prevention (DLP)
    - Advance Threat Protection (ATP)
- Regulatory Compliance
  - Ensured compliance with HIPAA and PCI standards.
  - Conducted merger and acquisition risk reviews, identifying and addressing critical third-party risks.
- Security Operations
  - Stopped active phishing attacks, safeguarding sensitive data.
  - Planned and executed ransomware mitigation strategies.
  - Designed and led security awareness programs, fostering a proactive security culture.

#### Walgreens | Senior Analyst, Informaiton Security | Lincolnshire, IL ####
Employed: Mar 2011 to May 2012

**Reason for leaving**

Walgreens decided to outsource information security jobs to offshore teams, my job was impacted.

**Role summary**

At Walgreens, I oversaw firewall changes, audited rules for risks and redundancies, and played a key role in the change management team, reviewing and authorizing critical system changes. I managed the jump server environment, ensuring secure access and maintaining comprehensive audit trails. Additionally, I configured and managed Blue Coat proxy servers, safeguarding key systems, including the Walgreens retail website, which generated an estimated $35,000 per minute.

My role extended to supporting major projects, including implementing the McAfee Network Security Platform (NSP) and reviewing the Microsoft Office 365 migration plan, where I resolved a critical design flaw that kept the project on track.

**Key Accomplishments**
- Identified and resolved operational inefficiencies, saving Walgreens $287,000 annually.
- Redesigned the Microsoft Office 365 migration plan, addressing critical design flaws and ensuring timely project completion.
- Managed and audited enterprise firewalls (Check Point, Juniper, Fortinet, Cisco), ensuring robust network security.
- Configured and managed Blue Coat proxy servers, protecting systems like Walgreens' retail website, which generated an estimated $35,000 per minute.
- Implemented McAfee M-8000 and M-6050 NSP intrusion detection and prevention systems, enhancing security posture.
- Conducted compliance reviews and managed change control processes, maintaining regulatory standards and minimizing risks.
- Managed jump server environments, ensuring secure access and maintaining audit trails for all changes and activities.
- Developed and maintained complex proxy scripts, ensuring secure and efficient internet access for critical systems.
- Provided Tier 3 support for firewalls, proxies, and POS systems, resolving critical issues and maintaining uninterrupted operations.
- Conducted security audits and identified vulnerabilities, ensuring adherence to enterprise security policies.

**Skills required for role**
- Firewall Management (Check Point, Juniper, Fortinet, Cisco)
- Blue Coat Proxy Configuration and Management
- Intrusion Detection & Prevention (McAfee NSP)
- Compliance Auditing and Change Management
- Jump Server Access Control and Audit Trail Management
- Security Awareness and Risk Mitigation
- Strategic Planning and Infrastructure Oversight
- Root Cause Analysis and Problem Solving
- Microsoft Office 365 Migration Expertise
- Proxy Scripting and Secure Internet Access
- Data Analytics and Business Continuity
- Technical Communication and Team Collaboration
"""

# Flask route for handling chatbot requests
# Flask route for handling chatbot requests
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json  # Get JSON data from the request
        if not data or 'prompt' not in data:
            return jsonify({"error": "Invalid request. 'prompt' key is missing or empty"}), 400

        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt cannot be empty"}), 400

        # Combine context with user's question
        combined_prompt = f"{documents_context}\nUser's Question: {prompt}"

        # Use OpenAI API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are Ask_Tedbot, a GPT designed to emulate Ted Summey, his experiences, and professional expertise. "
                    "Answer questions with clarity, precision, and professionalism. Blend humor, wit, and expertise "
                    "to keep responses engaging while providing valuable insights. Always limit your responses to 100 words or fewer."
                )},
                {"role": "user", "content": combined_prompt}
            ]
        )
        chatbot_response = response["choices"][0]["message"]["content"]
        return jsonify({"response": chatbot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
