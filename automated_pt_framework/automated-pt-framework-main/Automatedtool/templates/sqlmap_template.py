import subprocess
import logging

def execute_sqlmap(target, test_level=1, risk_level=1, additional_flags=None):
    """
    Execute customizable SQLMap scan with user-defined options.

    Args:
        target (str): Target URL for SQL injection testing.
        test_level (int): SQLMap test level (1-5, default: 1).
        risk_level (int): SQLMap risk level (1-3, default: 1).
        additional_flags (str): Extra SQLMap flags (e.g., '--dbs' to enumerate databases).
    """
    # Prepare the basic SQLMap command
    command = ['sqlmap', '-u', target, '--level', str(test_level), '--risk', str(risk_level)]
    
    # Add any additional flags if provided
    if additional_flags:
        command += additional_flags.split()

    print(f"Initiating SQLMap scan on {target} with options: {command}")
    
    try:
        # Execute the SQLMap scan and capture the output
        result = subprocess.run(command, capture_output=True, text=True, timeout=600)
        
        # Output the scan results
        print(result.stdout)
        
        # Log the scan output
        logging.info(f"SQLMap scan results: {result.stdout}")
    
    # Handle timeout scenario
    except subprocess.TimeoutExpired:
        print(f"SQLMap scan on {target} timed out.")
        logging.error("SQLMap scan timed out.")
    
    # Handle general exceptions
    except Exception as error:
        print(f"An error occurred: {error}")
        logging.error(f"SQLMap scan failed with error: {error}")

if __name__ == "__main__":
    # Gather user inputs
    target = input("Enter the target URL: ")
    test_level = input("Enter SQLMap test level (default 1): ") or 1
    risk_level = input("Enter SQLMap risk level (default 1): ") or 1
    additional_flags = input("Enter additional flags (optional): ")

    # Execute the SQLMap scan with provided inputs
    execute_sqlmap(target, test_level, risk_level, additional_flags)
