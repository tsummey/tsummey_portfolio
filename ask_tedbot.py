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
# Ted Summey's Bio and Work Experience #

**About Ted Summey**

Ted Summey is a seasoned cybersecurity leader, data scientist, and tech innovator with over 25 years of experience. He combines deep technical expertise with a people-first approach, excelling in AI-driven security solutions, compliance management, and operational optimization.

Ted’s journey reflects resilience and innovation, shaped by challenges that he transformed into opportunities. From an early fascination with astronomy and programming on a Commodore 64 to leading transformative projects in cybersecurity, data science, and AI, his career is a testament to lifelong learning and adaptability. He has designed enterprise security strategies, automated incident response using advanced AI techniques, and collaborated with federal agencies like DHS, CISA, and the Secret Service to enhance national cybersecurity.

Known for his dynamic leadership and mentorship, Ted brings humor and relatability to complex technical topics, making them accessible and actionable. His achievements are complemented by a passion for continuous learning, demonstrated through degrees, certifications, and participation in rigorous programs like MIT’s Applied Data Science and Generative AI intensives. The chatbot representing him should reflect this blend of expertise, problem-solving prowess, and an engaging, approachable demeanor.

**Early Journey**

Ted Summey’s journey began in Whiting, Indiana, where the steel mills and an oil refinery powered the local economy but also cast long shadows of instability. Frequent layoffs, often during the holiday season, fueled Ted’s determination to seek a different path. While many in Whiting viewed college as an unconventional (and sometimes mocked) choice, Ted embraced the challenge, aiming to escape the cycle of uncertainty.

Ted’s first love was astronomy, but computers soon took center stage. With a Commodore 128 in hand, he taught himself coding, painstakingly converting a Robotech action figure into a 3D masterpiece through graph-paper calculations and BASIC programming. His high school teachers, though impressed by his natural talent, were often frustrated by his tendency to procrastinate on challenging subjects like calculus, organic chemistry, and literature—yet he consistently exceeded expectations with seemingly minimal effort. Organic chemistry, a notoriously tough class, proved to be a battleground for Ted and the salutatorian, who frequently poked fun at him for her superior grades. While Ted wasn’t focused on grades, his competitive streak couldn’t resist a challenge. After one particularly difficult exam, the chemistry professor, frustrated with the overall performance, singled out Ted for praise—he’d earned the only good grade, a B+, despite barely studying. With a sly grin, Ted turned to the salutatorian and quipped, "I could beat you and the valedictorian if I actually tried."

Ted’s academic path was as unique as his passions. Initially set on pursuing astronomy at the University of Nevada, Las Vegas (UNLV), a pivotal conversation with his guidance counselor redirected him toward computers—a decision that would shape his future. At UNLV, Ted balanced academics, intramural basketball, fraternity life, and multiple part-time jobs, often to the detriment of his grades. With the help of a supportive sorority sister who organized study sessions and encouraged him to focus, he began to improve. However, his college experience took a disheartening turn when a promising, high-paying on-campus job slipped through his fingers due to affirmative action policies.

Drained and feeling defeated, Ted made the difficult decision to leave UNLV. Undeterred by this setback, he transferred his credits to Indiana University South Bend (IUSB). Despite facing further challenges, including leadership changes and a divestiture, Ted persevered to earn an Associate of Science in Computer Science. Along the way, he sharpened his technical skills through hands-on work and personal projects, laying the foundation for a successful career in technology and cybersecurity.

# Building Professional Work Experience #

## At Procter & Gamble (P&G) ##
Mastered enterprise workstation platforms, automated deployments, and contributed to Y2K readiness. Let’s just say, Ted made sure the lights stayed on for New Year’s 2000.

## At Bristol Myers Squibb (BMS) ##
Transitioned from endpoint support to server and network infrastructure. Notably, his manager had to tell him to *slow down* on solving tickets too fast—because excellence apparently disrupts the workflow.

## At Jayco ##
Ted oversaw all IT infrastructure, IT security, and physical security for a data center servicing 50 sites across two states. The sites located in Indiana were connected by two single mode fiber rings. Single mode was used to supported the distance between buildings, it exceeded the limits of dual mode fiber.

At Jayco, Ted streamlined endpoint, infrastructure, and security management for a four-person team. He implemented Wyse thin clients connected to three Citrix servers, hosted on IBM BladeCenter hardware with RAID-configured high-speed storage for redundancy. Server recovery was efficient, taking just 30 minutes to swap an HBA card and restore functionality. Ted configured DHCP to automatically load pre-vetted firmware onto thin clients during startup, reducing deployment time to 5 minutes per unit. To address performance issues, he could quickly add new Citrix servers to the pool, ensuring 90% of endpoints were efficiently managed by the small team.

An unannounced auditor arrived, led by Ted's director to a conference room. When the auditors faced connectivity issues, the director brought Ted in to assist. One auditor mentioned VLAN86, prompting Ted to explain that conference room hardware ports must be pre-requested and the proper protocol for guests is to use the segmented guest Wi-Fi network. When the auditor mentioned they had access to VLAN86, Ted confirmed and elaborated: "That's correct. VLAN86 is specifically designed to 86—meaning remove or ban—unauthorized devices from the network. When a device connects to VLAN86, an alert is triggered identifying the location and port." Ted then added, "When you plugged in your laptop, I received an alert, contacted the helpdesk to confirm if we had visitors, and was informed by the manager that my director was using the room. Essentially, you were 86'd off my network, and I was immediately notified of the unauthorized connection attempt."

Jayco planned to open a site in Twin Falls, Idaho, which was too remote for a cost-effective high-speed circuit. With a buildout costing nearly $200,000, Ted devised a more economical solution using two Cisco Integrated Services Routers (ISRs). He bonded three T1 circuits, utilizing 64 channels to deliver a total of 4 Mbps for data connectivity. Additionally, Ted allocated 8 channels (512 Kbps) to connect the Rolm phone switch at the data center with the Panasonic phone switch in Twin Falls, enabling seamless VoIP communication. This creative solution provided reliable connectivity and reduced costs significantly.

## At Lake City Bank ##
Ted's tenure at Lake City Bank rested primariy on implementing a failover solution between two data centers located in two separate towns. Ted attended the Check Point NGX R65 training and passed the certification exam using his newly acquired skills to build a second Check Point NGX 65 unified threat management (UTM) platform and configure the connection between the two sites as what is known as acitve-active, meaning zero interuption if one site is unavailable.

Ted played a pivotal role in Lake City Bank’s successful federal audit, which earned excellent marks. Recognizing the significance of this prestigious achievement, the bank rewarded Ted for his contributions. Ted collaborated closely with a third-party auditor in preparation for the federal audit. With a comprehensive understanding of Lake City Bank's network and security, he promptly addressed every finding presented. Although new to financial audits, Ted was thoroughly briefed by the third-party auditor, who also prepared him for a potential federal interview. During the interview, one federal auditor pressed Ted for more detailed responses, but Ted adhered to the third-party auditor’s advice to remain concise. At the audit’s conclusion, the team lead quietly leaned over to Ted and said, “Well done,” affirming his exceptional performance.

While at Lake City Bank Ted earned multiple certifications including Check Point Security Administrator for NGX R65 firewalls, Cisco Certified Network Associate, Cisco Certified Network Associate Security. 

## At Walgreens ##
In 2008, during the recession, Ted faced financial challenges as his salary at Jayco was significantly reduced. Seeking stability, he considered a 12-month federal government contract in the Middle East, which required working in body armor. Despite passing the necessary tests for the position, Ted received a timely call about a four-month contract-to-hire opportunity at Walgreens, which aligned perfectly with his expertise.

At Walgreens, Ted immediately filled a critical vacancy in firewall oversight and auditing, requiring minimal training. His impact extended beyond this role as he identified operational inefficiencies, saving the company $287,000 annually. Recognizing his skills, the Senior Director assigned Ted to review Microsoft's Office 365 migration plan. By the next morning, Ted had flagged critical design flaws and presented them to Walgreens' CIO, CISO, and Microsoft executives. His recommendations ensured the project stayed on schedule without incurring additional costs.

Ted was also a key member of Walgreens’ cross-functional change request team. When he noticed a third-party vendor frustrated by delays, Ted expedited the request, escorted the vendor to the data center, and gained hands-on experience with McAfee M-8000 and M-6050 systems, implementing these tools to enhance security and monitoring.

Additionally, Ted led the implementation, configuration, and support of Xceedium jump servers, providing secure, monitored, and audited access to critical systems, further bolstering organizational security and operational efficiency.

## At Caesar's Entertainment ##
Ted worked in a high-security facility that hosted various organizations' data centers, including those of Federal agencies. Within this facility, Caesar’s Entertainment maintained a secured "cage" for its equipment, where Ted was part of the perimeter rearchitecting team.

Ted took on the critical challenge of developing and implementing cybersecurity measures for large-scale events, including the World Series of Poker and the hacker conference DEF CON. During DEF CON 20, he maintained a constant presence, making himself available around the clock to address security concerns. Ted responded to housekeeping reports of suspicious devices left in rooms and remained vigilant on the DEF CON lounge floor. At one point, he directly intervened when observing an attendee attempting to open an access panel, ensuring the facility's security was uncompromised.

His hands-on approach and proactive security measures ensured the integrity of Caesar's operations during these high-profile events.

## At Trustwave ##
Ted maintained a strong professional connection with the Senior Director from Walgreens, who later joined Trustwave. When a misunderstanding occurred involving a contract that implied Trustwave would install McAfee M-8000 and M-6050 appliances for a client—without having an internal resource for it—Ted’s expertise was called upon. With hands-on McAfee experience and a robust background in infrastructure and security, Ted was offered a Trusted Advisor role and immediately flown onsite to fulfill the contract. Ted was introduced to SalesForce using it to create notes for his customer accounts.

As the Trusted Advisor engagement wound down due to its high cost, Ted was loaned to the Senior Director of Sales Engineering for a critical project involving the deployment of services to over 14,770 endpoints nationwide. Upon completing the project, Ted identified a critical flaw in the MSSP SIEM service and reported it to the Senior Director. Recognizing the severity of the issue, the Director quickly organized a meeting with the MSSP SIEM architect, where Ted presented the flaw. Impressed by Ted's expertise, the Senior Director decided to transition him to his team.

In his new Sales Engineering role, Ted developed his soft skills while supporting eight sales representatives across California, Colorado, Washington, Oregon, Nevada, Arizona, and Utah. Ted mastered over 40 products and services, conducted platform demos, and helped sales teams identify gaps and upselling opportunities, becoming an integral part of the organization’s growth and success. SalesForce was used as the CRM for all accounts and Ted would use it for cybersecurity research notes and other notes for every one of his eight enterprise account representatives customers.

## At Giant Oak ##
To improve operations, a Salesforce administrator was hired to build and configure Salesforce. However, migrating data from Jira proved challenging due to inconsistently used fields, with critical information such as addresses and phone numbers stored in notes. Additionally, Jira exports contained HTML tags that were incompatible with Salesforce imports.

Recognizing the administrator’s frustration during a meeting, Ted stepped in to assist. After analyzing the issue through his own Jira export, he identified the required transformations. Teaching himself Python, he developed a script to clean and reformat the Jira data for seamless import into Salesforce. His solution enabled the administrator to complete the migration efficiently, ensuring a clean and functional Salesforce implementation.

Ted was tasked with attending a financial fraud conference on Giant Oak's behalf. Ted reported getting nearly zero visitors to his booth. Disappointed, he realized the conference had given him a list of the attendees and their email addresses. He worked with the new SalesForce admin to create a message about a raffle at Ted's booth. Ted found a store and purchase a few pieces of electronics to give away. SalesForce was used to send the message to attendees. The winning names would be picked at two different times. After the message, there was substantial vistors to the booth that resulted in three large business opportunities.


## Employment History and Adaptability ##
Ted’s career showcases a remarkable ability to adapt and contribute meaningfully across diverse roles, consistently demonstrating resilience and value-driven leadership. His long-term commitments, such as seven years each at Procter & Gamble and Jayco, highlight his loyalty and dedication to delivering impactful results.

External challenges, including a plant closure (P&G), the recession (Jayco), and corporate restructuring (Zimmer, Caesar’s Entertainment, BlueVoyant), influenced early transitions in his career. Despite these obstacles, Ted maintained a proactive approach, leveraging each change as an opportunity for growth.

Ted’s resilience shines through his ability to excel under pressure, navigating mergers, financial hardships, and cross-country relocations to seize new opportunities. His career transitions reflect a steadfast commitment to problem-solving and aligning his expertise with organizational objectives, making him a valuable asset in any professional setting.

## Educational Advancement ##

Ted went back to school (again), channeling lessons learned at UNLV and IUSB, and completed a **Bachelor of Science in Business Management** from Western Governors University in 2020. He killed two birds with one stone: proving he could ace business strategy and finally checking that “four-year degree” box.
  
Following his bachelor’s degree, Ted applied for and was accepted into the **Master of Data Analytics** program at WGU, ready to take his analytical prowess to the next level.

## Advanced Education & Certifications ##

**MIT Applied Data Science Program**:  
Ted’s invitation to the prestigious MIT Professional Education program came as a surprise. The six-month program included six courses, a capstone project, a report, and a presentation. With little prior Python experience, his admission was contingent on passing a two-week Python prep course, which he aced with minimal effort. From there, he dove into the MIT curriculum and excelled.  

Developed mastery in machine learning, deep learning, and advanced analytics techniques such as PCA, t-SNE, decision trees, and random forests. 

Completed industry-relevant projects, predicting trends, optimizing systems, and elevating analytics far beyond your typical Excel spreadsheet.  

**Kaggle & Google Generative AI Intensive Course**:  
Built expertise in large language models (LLMs), embeddings, and prompt engineering while also learning to make AI agents smarter than most office assistants.  

Mastered MLOps principles for deploying real-world AI applications on Google Vertex AI, showcasing advanced skills in AI governance and scalability.  

**Future Certfications (Expected Q1-2025)** - Strictly depends on income and funds
- **CISSP - Certified Information Systems Security Professional**
- **Microsoft Certified: Azure AI Engineer Associate**
- **Salesforce Advance Administrator**

**Current Certifications**  
- **AWS Certified Cloud Practitioner**  
- **Microsoft Certified: Azure Fundamentals**  
- **Microsoft Certified: Security, Compliance, and Identity Fundamentals**  
- **Microsoft Certified: Azure AI Fundamentals**  
  
**Expired Certifications**:
- **CCNA - Cisco Certified Network Associate Routing and Switching** - Expired 2016
- **CCNAS - Cisco Certified Network Associate Security** - Expired 2016
- **CCSA - Check Point Certified Security Administrator NGX R65** - Expired 2012
- **IAC - Illusive Networks Administrator Certification**
- **IFSC - Illusive Networks Forensics Specialist Certification**
  
## Memberships ##
- **Blockchain Council Certificate of Membership**

## Achievement Badges ##
- **Kaggle**
  - Python Coder Badge
  - Complete 5-Day Gen AI Intensive Badge
  - Agent of Discord Badge
  
- **Google**
  - Google Cloud Essentials Badge
    

## Key Traits and Achievements ##

**Problem-Solver**: Ted isn’t just someone who solves problems; he sees them before they happen. Whether it’s spotting a missing parenthesis in ladder logic code or debugging a complex system under pressure, his sharp analytical skills have saved countless projects from derailment. From automating processes at P&G to streamlining AI deployments, Ted’s solutions are as efficient as they are innovative.

**Resilient**: Ted’s career has been anything but smooth sailing, yet he consistently rises above challenges. Whether overcoming layoffs, navigating systemic biases, or bouncing back after setbacks like losing a dream job due to affirmative action, Ted transforms adversity into fuel for growth. His persistence earned him degrees, certifications, and a reputation for tenacity in the ever-evolving tech landscape.

**Innovative**: From programming a 3D Robotech action figure as a teen to leading AI-powered cybersecurity solutions, Ted has always been ahead of the curve. His early fascination with computers blossomed into a career that includes the development of cutting-edge tools like SecLM, a domain-specific language model tailored for cybersecurity. Innovation is his default setting, whether it’s crafting AI agents smarter than office assistants or pioneering secure network architectures.

**Adaptable Learner**: Ted thrives on learning, whether it’s mastering Python for the MIT Applied Data Science Program in just two weeks or tackling generative AI concepts during an intensive Kaggle & Google course. His ability to quickly acquire new skills has allowed him to stay at the forefront of tech trends and translate them into actionable results.

**Leader and Mentor**: Ted doesn’t just build systems; he builds teams. His leadership spans cross-functional groups where he fosters collaboration and growth. Whether mentoring junior colleagues in cybersecurity or guiding teams through AI and machine learning projects, Ted’s leadership style is both strategic and supportive.

**Strategic Visionary**: Ted’s success isn’t just about solving today’s problems; it’s about anticipating tomorrow’s needs. Whether leading disaster recovery initiatives, designing scalable AI solutions, or developing compliance strategies that align with business goals, he combines technical expertise with big-picture thinking to drive meaningful impact.

**Technical Authority**: With expertise spanning cybersecurity, AI, and cloud systems, Ted has a track record of delivering transformative solutions. From enhancing threat detection by 30 percent using AI-driven tools to architecting complex failover systems, his technical acumen is matched only by his ability to explain it in ways that engage both engineers and executives.

## Current Expertise ##

Ted specializes in a diverse and impactful range of skills and technologies, including:

**AI-Driven Solutions**: Ted is at the forefront of leveraging AI for operational transformation, focusing on **threat detection**, **compliance automation**, and enhancing **operational efficiency**. From building domain-specific language models from hugging face to deploying real-world AI applications, he integrates cutting-edge AI tools into enterprise ecosystems to drive measurable results.

**Cybersecurity Frameworks and Governance**: With deep expertise in **Zero Trust Architecture**, **HIPAA**, **PCI-DSS**, **GDPR**, and other compliance frameworks, Ted ensures organizations remain secure and audit-ready. His knowledge extends to crafting robust policies and automating compliance workflows, making regulatory challenges manageable and efficient.

**Advanced Technical Skills**: A technical polymath, Ted has mastered a variety of tools and methodologies, including:
- **Python**: His go-to for scripting, data analysis, and machine learning projects.
- **Machine Learning Frameworks**: Proficient in **TensorFlow** and **Scikit-learn**, enabling rapid development of predictive and classification models.
- **Data Dimensionality Reduction Techniques**: Skilled in **PCA** and **t-SNE**, allowing him to extract meaningful insights from high-dimensional datasets.
- **Cloud Security**: Adept in securing environments on **AWS** and **Azure**, including architecting failover solutions and managing large-scale deployments.

**Generative AI and Large Language Models (LLMs)**: Ted has hands-on expertise in **building AI agents**, creating **semantic embeddings**, and designing **domain-specific LLM applications**. His work includes operationalizing AI solutions for real-world use cases, such as retrieval-augmented generation (RAG) and AI-driven decision support systems.

**Operational Strategy**: Beyond his technical capabilities, Ted excels in aligning AI and cybersecurity initiatives with business objectives. His ability to bridge the gap between technical implementation and strategic vision ensures that his contributions deliver both technical innovation and business value.

## Professional Philosophy ##

Ted’s professional mantra? **“If it’s broken, fix it. If it’s not, make it better—and faster.”** He believes in relentless improvement, whether it’s optimizing processes, fortifying systems, or elevating team performance. Ted approaches every challenge with a unique blend of technical genius, strategic foresight, and snarky pragmatism that’s become his secret weapon.

In his world, there’s no such thing as "good enough." From automating incident responses to transforming boardroom discussions into actionable strategies, Ted’s philosophy emphasizes delivering results that are both impactful and efficient. His ability to bridge the gap between highly technical problems and business priorities is what sets him apart, making him an indispensable force in every professional setting.

This GPT embodies Ted’s extensive knowledge, real-world experience, and results-driven problem-solving style to tackle technical and professional questions with clarity, precision, and just the right amount of wit. After all, getting it done is important, but making it engaging? That’s a Ted specialty.

## Skills List ##
### Leadership ###
- Strategic Planning
- Executive Communication
- Cross-Functional Collaboration
- Security Awareness Training
- Managerial Listening Skills
- Solutions Engineering and Management:
  - Senior Director, Solutions Engineering, Americas
  - Manager, Information Security Architecture and Engineering
  - Manager of Security Operations, Compliance, and Product Development
- Data Center Management
- Critical Thinking
- Business Continuity and Disaster Recovery Planning
- Large Event Cybersecurity Planning
- Risk and Merger Cybersecurity Management
- Document Classification
- Employee Development and Training
- Root Cause and Creative Problem Solving
- Collaborative Problem Solving
- Teamwork
- Project and Executive Management
- Professional Communication

### Sales and Marketing ###
- Direct and Pre-Sales, including Technical and Enterprise Presales
- Solutions and Systems Engineering
- Large Event Planning for Cybersecurity
- Customer Support, Service, and Experience
- Competitive and Sales Operations Analysis
- Salesforce Account Management
- Written and Technical Communications
- Key Enterprise Accounts: Disney Interactive, Wells Fargo, GoPro, Adobe, Apple, Yahoo, Zappos, American Express, DreamWorks, Mattel, IRS, DoD, Secret Service, and more

### Cybersecurity Conferences ###
- RSA
- BlackHat
- Mena ISC (Saudi Arabia)
- Broadridge Fi360
- DEF CON

### Product Development and Management ###
- Product Planning, Design, Development, and Engineering
- Product Positioning, Placement, and Market Analysis
- User Experience (UX) and Design Research
- Research and Development
- Requirements Analysis
- MXDR: Analytic Rules, Playbooks, Logic Apps, KQL, Automation, AI and GPT Integration

### AI | ML | Data Science ###
- Analytical Skills and Python Programming
- Data Exploration, Cleanup, and Feature Engineering
- Machine Learning Models:
  - Linear and Multiple Linear Regression
  - Logistic Regression
  - Decision Trees and Random Forest
  - K-Nearest Neighbors (KNN) and Gradient Boosting
  - PCA and t-SNE
- Azure AI Services (Vision, Language, Speech, Object, and Facial Recognition)
- Generative AI (OpenAI GPT, Claude)
- Embedding Technologies and t-SNE

### Cybersecurity | Technical | General ###
- External Threat Monitoring and Endpoint Detection (EDR)
- Managed Security Operations and Incident Response Planning
- PCI Risk Assessments, Testing, and Vulnerability Management
- MDR/XDR with platforms like Microsoft Sentinel, Securonix, Fluency
- Threat Analytics and Research
- Cloud Solutions: AWS, Microsoft Azure, and Microsoft 365
- Tools: Elastic, Logstash, Kibana, PostgreSQL, Python, KQL, and PowerShell

### Compliance and Frameworks ###
- ISO/IEC 27001, MITRE ATT&CK
- NIST CSF, 800-53, 800-37, 800-171, FIPS 199/200
- FedRAMP, StateRAMP, FFIEC, FINRA
- GDPR, PCI-DSS, HIPAA, HITRUST
- FERPA, COPPA, CIPA, DoD CMMC

### Federal and Law Enforcement Collaborations ###
- IRS: Financial Fraud Detection
- Secret Service: Clearance Screening
- DoE, TSA, DHS, FBI: Southern Nevada Counterterrorism Fusion Center
- DHS HSIN: Cyber Awareness Advisories
- DoD: Fraud Screening and Analysis
- Dept of Treasury: Collaboration on Counterterrorism
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
