import subprocess

def run_nmap_scan(target_ip):
    print(f"Starting Nmap scan on {target_ip}...")
    
    # Nmap command with options
    nmap_command = ['nmap', '-sV', target_ip]

    try:
        # Run the Nmap scan with a timeout of 300 seconds (5 minutes)
        result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=300)
        
        # Print stderr if there's an error during the scan
        if result.stderr:
            print(f"Error during Nmap scan: {result.stderr}")
            return None
        
        # Print stdout if the scan is successful
        if result.stdout:
            print(f"Nmap scan completed successfully for {target_ip}.")
            return result.stdout
        else:
            print("Nmap scan completed, but no output was returned.")
            return None

    except subprocess.TimeoutExpired:
        print("Nmap scan timed out after 300 seconds.")
        return None

    except subprocess.SubprocessError as e:
        print(f"An error occurred while running the Nmap scan: {str(e)}")
        return None

# Main function to call the Nmap scan
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    
    # Validate input
    if not target_ip:
        print("Error: No target IP provided.")
    else:
        # Run the Nmap scan and capture the output
        scan_result = run_nmap_scan(target_ip)
        
        # If scan_result is not None, print the result
        if scan_result:
            print("\nNmap Scan Output:\n")
            print(scan_result)
        else:
            print("Nmap scan failed or produced no output.")
