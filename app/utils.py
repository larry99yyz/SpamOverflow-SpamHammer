import subprocess

def scan_email(email_id: str) -> str:
    result = subprocess.run(['spamhammer', email_id], capture_output=True, text=True)
    output = result.stdout.strip()
    return output
