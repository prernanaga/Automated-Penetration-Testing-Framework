import os
from datetime import datetime

def get_consent():
    """
    Function to gather client consent for penetration testing.
    Returns True if consent is obtained, False otherwise.
    """

    client_name = input("Enter the client's name: ")
    target_ip = input("Enter the target IP address: ")
    testing_scope = input("Enter the testing scope (e.g., network, web application): ")

    consent = input(f"Do you, {client_name}, give consent for penetration testing on IP {target_ip} for {testing_scope}? (yes/no): ").lower()

    if consent == 'yes':
        # Save the consent to a file
        consent_directory = "consent_forms"
        if not os.path.exists(consent_directory):
            os.makedirs(consent_directory)

        consent_file = f"{consent_directory}/consent_{client_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(consent_file, 'w') as f:
            f.write(f"Client Name: {client_name}\n")
            f.write(f"Target IP: {target_ip}\n")
            f.write(f"Testing Scope: {testing_scope}\n")
            f.write(f"Consent Given: Yes\n")
            f.write(f"Date: {datetime.now()}\n")

        print("Consent saved successfully.")
        return True
    else:
        print("Consent not obtained.")
        return False
