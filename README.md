# Automated-Penetration-Testing-Framework 
Automated pen testing is when system security architecture vulnerabilities are detected using integrated pen testing tools. It is the result of ongoing developments in machine learning. It is more advanced and efficient than vulnerability scanning, which examines computer networks to identify security weaknesses that can leave organizations exposed to cyber threats. 
The Automated Penetration Testing Framework is designed to streamline a range of security evaluations, such as network scanning, SQL injection analysis, exploitation, and post-exploitation. This framework combines tools like Nmap, SQL Map, and Metasploit, offering a modular, adaptable, and automated solution for conducting penetration tests.

# Features of this Project:

1. Nmap Scanning Module: Conducts network scans to detect open ports and active services.
2. SQL Map Scanning Module: Automates testing for SQL injection vulnerabilities and retrieves data.
3. Exploitation Module: Utilizes Metasploit to automate exploits with flexible payload configurations.
4. Post-Exploitation Module: Performs post-exploitation tasks, including privilege escalation and setting up persistence.
5. Logging and Reporting: Logs all activities and generates a detailed report outlining the test results.
6. R-Based Access Control (RBAC): Implements secure user authentication and role-based permissions management.
7. Consent Management: Ensures adherence to legal requirements by obtaining formal client consent before starting any tests.

# Prerequisites are:

Before starting this project, make sure the following tools are installed on your system:

• Python 3.x: The framework is developed using Python.

• Nmap: Used for network scanning.

• SQL Map: Utilized for SQL injection testing.

• Metasploit Framework: Required for exploitation and post-exploitation tasks.

To install these tools on Kali Linux, run the following commands:

   => sudo apt update  
   => sudo apt install nmap  
   => sudo apt install sqlmap  
   => sudo apt install metasploit-framework

# Structure of the Project: 

(folders) - 

automated_pt_framework

automated-pt-framework-main

Automatedtool/

• consent_management.py => Manages client consent and permissions

• exploit_module.py => Handles automated Metasploit exploitation

• logging_setup.py => Configures logging for all actions

• master.py => Main script that orchestrates the entire process

• nmap_scan.py => Executes Nmap scans

• post_exploitation.py => Handles post-exploitation tasks

• sqlmap_scan.py => Runs SQLMap for SQL injection testing

• consent_forms/ => Stores saved consent forms

• pentest_framework.log => Logs activities during the test

• final_report.txt => Contains the final penetration test report

# Installation Guide:

1) First clone the repository in the local machine, and run the below-given command:
   
   git clone https://github.com/prernanaga/Automated-Penetration-Testing-Framework.git

3) Then go to the location where the file is saved in your Kali machine:
   
   cd Downloads/automated_pt_framework/automated-pt-framework-main/Automatedtool   (this path is according to my machine)

4) Installing Python Dependencies(if any): If your project has a requirements.txt file, install the necessary packages with:
   
   pip install -r requirements.txt
   
Set Permissions: Make sure you have the required permissions to run system-level tools like Metasploit, Nmap, and SQLMap.

4) Obtain Client Consent: Before starting any tests, you must collect and store the client's consent using the consent_management.py module:

   python3 consent_management.py
   
This script will prompt you to enter the client’s name, target IP address, and scope of testing. The consent information will be saved in a timestamped file within the consent_forms/ folder.

5) To initiate the penetration testing process, execute the master.py script:

   python3 master.py
   
This script will:

A. Authenticate the user using a hashed password.         

B. Request the target IP or URL for scanning. 

C. Perform Nmap scanning, SQLMap testing, exploitation, and post-exploitation steps in order. 

D. Log all activities and create a final report.

You can also run specific modules to perform particular tasks:

=> Run a Nmap scan: python3 nmap_scan.py

=> Run an SQLMap scan: python3 sqlmap_scan.py

=> Run the Exploitation Module: python3 exploit_module.py

6) Viewing Logs and Reports

All actions are logged in the pentest_framework.log file. The final penetration test report will be saved as final_report.txt.

#  Summary workflow of the scanning

=> Run the master.py script:
The framework will initiate by collecting client consent, authenticating the user, and starting the network scan using Nmap.

=> Perform SQL Injection Tests:
It will then conduct SQL injection testing with SQLMap, identifying and exploiting any vulnerabilities found.

=> Exploit Vulnerabilities:
Any discovered vulnerabilities will be exploited using Metasploit, automating the exploitation process. The information asked in the tool can be answered by running Metasploit on the machine.

=> Execute Post-Exploitation Tasks:
After exploitation, the framework will carry out post-exploitation tasks, such as privilege escalation and establishing persistence.

=> Generate Report and Log Activities:
Finally, it will compile a detailed report and log all activities throughout the testing process.

# Timeouts of each script: 

These are the maximum time taken - 

1. SQL Map: 1200
2. Nmap: 600
3. Exploitation: 1200
4. Post-exploitation: 1200
