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





