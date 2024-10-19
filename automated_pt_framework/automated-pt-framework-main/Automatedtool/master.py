import consent_management  
import nmap_scan
import sqlmap_scan
import exploit_module
import post_exploitation
import logging_setup as log
import getpass
import hashlib
import signal
import time

# In-memory user data
USERS_DB = {
    'admin': {
        'password': hashlib.sha256('adminpass'.encode()).hexdigest(),
        'role': 'admin'
    },
    'tester': {
        'password': hashlib.sha256('testerpass'.encode()).hexdigest(),
        'role': 'tester'
    }
}

# Timeout values in seconds
TIMEOUTS = {
    'nmap': 600,
    'sqlmap': 1200,
    'exploit': 1200,
    'post_exploitation': 1200,
    'overall': 3600  # 1 hour overall timeout
}

# Function to handle timeouts
def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

# Set the signal for the overall timeout
signal.signal(signal.SIGALRM, timeout_handler)

# Function to authenticate the user
def authenticate(username, password):
    if username in USERS_DB:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if USERS_DB[username]['password'] == hashed_password:
            return True, USERS_DB[username]['role']
    return False, None

# RBAC check function
def check_access(role, action):
    if role == 'admin':
        return True  # Admins can perform all actions
    elif role == 'tester' and action in ['nmap_scan', 'sqlmap_scan']:
        return True  # Testers can only perform scanning actions
    return False  # Unauthorized access

# Function to execute a customizable script
def run_custom_script(script_path):
    try:
        with open(script_path, 'r') as script_file:
            exec(script_file.read())  # Execute the custom script
        return True
    except Exception as e:
        print(f"Error executing custom script: {e}")
        return False

def log_and_execute(username, action, target, func, *args):
    """
    Log the action and execute the specified function.
    
    Args:
        username (str): The username of the user performing the action.
        action (str): The action being performed.
        target (str): The target of the action.
        func (callable): The function to execute.
        *args: Arguments to pass to the function.
    
    Returns:
        Any: Result of the executed function.
    """
    log.log_action(username, f"{action} started", target)
    result = func(*args)
    log.log_action(username, f"{action} completed", target)
    return result

def main():
    # Step 1: User authentication
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Authenticate user
    is_authenticated, role = authenticate(username, password)
    if not is_authenticated:
        print("Authentication failed. Exiting.")
        return
    print(f"Authentication successful. Logged in as {username} with role: {role}")

    # Step 2: Obtain consent for penetration testing
    if not consent_management.get_consent():
        print("Consent not obtained. Exiting.")
        log.log_action(username, "Consent not obtained", "")
        return
    log.log_action(username, "Consent obtained", "")

    # Step 3: Get target details
    target_ip = input("Enter the target IP address: ")
    target_url = input("Enter the target URL: ")

    # Ask user if they want to use custom scripts
    use_custom_scripts = {
        'nmap': input("Do you want to use a custom Nmap script? (yes/no): ").lower() == 'yes',
        'sqlmap': input("Do you want to use a custom SQLMap script? (yes/no): ").lower() == 'yes',
        'exploit': input("Do you want to use a custom Exploit script? (yes/no): ").lower() == 'yes',
        'post_exploit': input("Do you want to use a custom Post-Exploitation script? (yes/no): ").lower() == 'yes',
    }

    # Start the overall timeout
    signal.alarm(TIMEOUTS['overall'])

    try:
        # Step 4: Start Nmap scan
        if check_access(role, 'nmap_scan'):
            print("\nStarting Nmap scan...")
            signal.alarm(TIMEOUTS['nmap'])  # Set Nmap timeout
            
            nmap_result = (run_custom_script(input("Enter the path to your custom Nmap script: "))
                           if use_custom_scripts['nmap'] else nmap_scan.run_nmap_scan(target_ip))
            log_and_execute(username, "Nmap scan", target_ip, nmap_scan.run_nmap_scan, target_ip)
        else:
            nmap_result = "N/A"
            print("You do not have permission to run the Nmap scan.")

        # Step 5: Start SQLMap scan
        if check_access(role, 'sqlmap_scan'):
            print("\nStarting SQLMap scan...")
            signal.alarm(TIMEOUTS['sqlmap'])  # Set SQLMap timeout
            
            sqlmap_result = (run_custom_script(input("Enter the path to your custom SQLMap script: "))
                             if use_custom_scripts['sqlmap'] else sqlmap_scan.run_sqlmap_scan(target_url))
            log_and_execute(username, "SQLMap scan", target_url, sqlmap_scan.run_sqlmap_scan, target_url)
        else:
            sqlmap_result = "N/A"
            print("You do not have permission to run the SQLMap scan.")

        # Step 6: Run the exploit
        if check_access(role, 'exploit'):
            print("\nRunning exploit...")
            exploit_module_name = input("Enter the exploit module (e.g., exploit/unix/ftp/vsftpd_234_backdoor): ")
            payload_name = input("Enter the payload (e.g., payload/unix/reverse_perl): ")
            rport = input("Enter the remote port (e.g., 21): ")
            lhost = input("Enter your local IP address: ")
            lport = input("Enter your local port (e.g., 4444): ")

            signal.alarm(TIMEOUTS['exploit'])  # Set Exploit timeout
            
            exploit_result = (run_custom_script(input("Enter the path to your custom Exploit script: "))
                              if use_custom_scripts['exploit'] else exploit_module.run_exploit(
                                  module=exploit_module_name,
                                  payload=payload_name,
                                  rhost=target_ip,
                                  rport=rport,
                                  lhost=lhost,
                                  lport=lport))
            log.log_action(username, "Exploit completed", target_ip)
        else:
            exploit_result = False
            print("You do not have permission to run the exploit.")

        # Step 7: Post-exploitation
        if exploit_result:
            print("Exploit succeeded. Moving to post-exploitation...")
            session_id = input("Enter the session ID for post-exploitation: ")

            signal.alarm(TIMEOUTS['post_exploitation'])  # Set Post-exploitation timeout
            
            if use_custom_scripts['post_exploit']:
                run_custom_script(input("Enter the path to your custom Post-Exploitation script: "))
            else:
                log_and_execute(username, "Post-exploitation (Privilege Escalation)", target_ip,
                                post_exploitation.run_privilege_escalation, session_id)
                log_and_execute(username, "Post-exploitation (System Info)", target_ip,
                                post_exploitation.gather_system_info, session_id)
        else:
            print("Exploit failed. Skipping post-exploitation.")

        # Step 8: Generate the overall report
        print("\nGenerating final report...")
        report_content = f"""Penetration Testing Report
        Target IP: {target_ip}
        Target URL: {target_url}

        Nmap Scan Results:
        {nmap_result}

        SQLMap Scan Results:
        {sqlmap_result}

        Exploit Status: {'Succeeded' if exploit_result else 'Failed'}
        """

        # Save the final report
        with open("final_report.txt", "w") as report_file:
            report_file.write(report_content)
        print("Final report saved to final_report.txt")

    except TimeoutError as e:
        print(f"Error: {str(e)}")
        log.log_action(username, f"Operation timed out: {str(e)}", target_ip)

    finally:
        signal.alarm(0)  # Disable the alarm

if __name__ == "__main__":
    main()
