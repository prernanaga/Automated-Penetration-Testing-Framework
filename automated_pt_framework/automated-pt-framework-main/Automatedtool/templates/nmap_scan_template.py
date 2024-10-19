import subprocess
import logging

def execute_nmap_scan(target, scan_options='-sV', port_range=None, additional_flags=None):
    """ 
    Run a flexible Nmap scan with user-specified options.
    
    Args:
        target (str): Target IP address or hostname.
        scan_options (str): Nmap scan options (e.g., -sV, -sS, -A, etc.).
        port_range (str): Port range to scan (e.g., '80,443' or '1-65535').
        additional_flags (str): Additional Nmap flags for the scan (optional).
    """
    # Base command for Nmap
    nmap_command = ['nmap', scan_options]

    # Include port range if provided
    if port_range:
        nmap_command += ['-p', port_range]
    
    # Add additional flags if provided
    if additional_flags:
        nmap_command += additional_flags.split()

    # Append the target IP or domain
    nmap_command.append(target)

    # Print command details for user reference
    print(f"Executing Nmap scan on {target} with command: {nmap_command}")
    
    try:
        # Run the Nmap command with a 10-minute timeout
        result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=600)
        
        # Display and log the scan results
        print(result.stdout)
        logging.info(f"Nmap scan results: {result.stdout}")
        
    except subprocess.TimeoutExpired:
        # Handle the timeout case
        print(f"Nmap scan on {target} timed out after 600 seconds.")
        logging.error(f"Nmap scan on {target} timed out.")
        
    except Exception as err:
        # Handle any other errors during the scan
        print(f"An error occurred: {err}")
        logging.error(f"Failed to execute Nmap scan: {err}")

if __name__ == "__main__":
    # Gather input from the user
    target_ip_or_hostname = input("Enter the target IP address or hostname: ")
    scan_options = input("Enter Nmap scan type (default -sV): ") or '-sV'
    port_range = input("Enter port range (optional): ")
    additional_flags = input("Enter additional flags (optional): ")

    # Execute the Nmap scan with the provided inputs
    execute_nmap_scan(target_ip_or_hostname, scan_options, port_range, additional_flags)
