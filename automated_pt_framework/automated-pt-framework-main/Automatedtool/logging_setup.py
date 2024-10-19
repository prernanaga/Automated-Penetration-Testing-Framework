import logging
import configparser
from datetime import datetime

# Set up configuration for logging
def setup_logging(config_file='config/logging.conf'):
    """
    Set up logging configuration for the framework based on a configuration file.

    Args:
        config_file (str): Path to the logging configuration file.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Read configuration from the specified file
    config = configparser.ConfigParser()
    config.read(config_file)

    log_file = config.get('logging', 'log_file', fallback='pentest_framework.log')
    log_level = config.get('logging', 'log_level', fallback='INFO').upper()
    
    # Define logging format and log file location
    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    return logging.getLogger()

# Function to log actions
def log_action(username, action, target_ip=None):
    """
    Log an action performed by a user or client.

    Args:
        username (str): The username or client name.
        action (str): The action performed.
        target_ip (str, optional): The target IP address. Defaults to None.
    """
    if target_ip:
        logging.info(f"User {username} performed {action} on {target_ip}")
    else:
        logging.info(f"User {username} performed {action}")

# Example usage: logging an action when consent is saved
if __name__ == "__main__":
    logger = setup_logging()
    log_action("ExampleClient", "Consent saved", "192.168.0.10")
