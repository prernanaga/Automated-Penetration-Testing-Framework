import subprocess

def run_sqlmap_scan(target_url):
    """
    Scan a target URL using SQLMap.

    Args:
        target_url (str): The URL to scan.

    Returns:
        str: The output of the SQLMap scan or None if an error occurs.
    """
    print(f"Scanning {target_url} with SQLMap...")

    # SQLMap command with extended options for a comprehensive scan
    sqlmap_command = [
        'sqlmap', '-u', target_url, '--batch', '--level', '5', '--risk', '3',
        '--dump-all', '--dbs', '--random-agent'
    ]

    try:
        # Execute the SQLMap command
        result = subprocess.run(sqlmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=600)

        # Check for errors during SQLMap execution
        if result.stderr:
            print(f"Error occurred during SQLMap scan: {result.stderr.strip()}")
            return None
        
        # Return the results of the scan
        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        print("SQLMap scan timed out after 600 seconds.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def save_results(scan_results, filename='sqlmap_results.txt'):
    """
    Save scan results to a file.

    Args:
        scan_results (str): The results of the scan to save.
        filename (str): The name of the file to save results to.
    """
    with open(filename, 'w') as f:
        f.write(scan_results)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    scan_results = run_sqlmap_scan(target_url)

    if scan_results:
        save_results(scan_results)
        print("Scan completed and results saved to sqlmap_results.txt")
    else:
        print("SQLMap scan did not complete successfully.")
