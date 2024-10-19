import subprocess
import logging

def execute_nmap(target, scan_mode='-sV', port_range=None, additional_options=None):
    """ 
    Run a customizable Nmap scan with user-defined parameters.
    
    Args:
        target (str): IP address or hostname of the target.
        scan_mode (str): Nmap scan mode (e.g., -sV, -sS, -A, etc.).
        port_range (str): Specific ports or ranges (e.g., '80,443' or '1-65535').
        additional_options (str): Additional Nmap options for flexibility (e.g., '-T4').
    """
    # Base Nmap command
    nmap_command = ['nmap', scan_mode]

    # Add the port range if specified
    if port_range:
        nmap_command += ['-p', port_range]

    # Add additional options if provided
    if additional_options:
        nmap_command += additional_options.split()

    # Append the target IP or hostname
    nmap_command.append(target)

    # Display the command being executed
    print(f"Executing Nmap scan on {target} with command: {nmap_command}")
    
    try:
        # Run the command with a timeout of 600 seconds (10 minutes)
        result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=600)
        
        # Display and log the scan results
        print(result.stdout)
        logging.info(f"Nmap scan output: {result.stdout}")
    
    except subprocess.TimeoutExpired:
        # Handle timeout scenario
        print(f"Nmap scan on {target} timed out.")
        logging.error("Nmap scan timeout occurred.")
    
    except Exception as err:
        # Catch and log any other errors
        print(f"An error occurred: {err}")
        logging.error(f"Error executing Nmap scan: {err}")

if __name__ == "__main__":
    # User inputs for target, scan mode, port range, and additional options
    target = input("Enter the target IP address or hostname: ")
    scan_mode = input("Enter Nmap scan type (default -sV): ") or '-sV'
    port_range = input("Enter port range (optional): ")
    additional_options = input("Enter additional flags (optional): ")

    # Run the scan with the provided inputs
    execute_nmap(target, scan_mode, port_range, additional_options)
