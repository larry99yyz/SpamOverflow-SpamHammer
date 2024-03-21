# app/utils.py
import subprocess

def scan_email(email_id: str) -> str:
    # Call the spamhammer tool to scan the email
    # Replace 'spamhammer' with the appropriate path to the spamhammer executable
    result = subprocess.run(['spamhammer', email_id], capture_output=True, text=True)
    output = result.stdout.strip()
    return output
