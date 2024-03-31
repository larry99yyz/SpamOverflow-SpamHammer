from flask import Flask, request, jsonify
from app.models import EmailScanRequest
from app.utils import scan_email

app = Flask(__name__)

@app.route('/scan/', methods=['POST'])
def scan_email_endpoint():
    data = request.json
    try:
        email_request = EmailScanRequest(**data)
        result = scan_email(email_request.email_id)
        
        if result == "SPAM":
            notification_message = f"Email '{email_request.email_id}' detected as spam. Moved to trash."
            # Code for notifying owner_email
            # send_notification(email_request.owner_email, notification_message)
        else:
            notification_message = f"Email '{email_request.email_id}' is not spam."
            # Code for notifying owner_email
            # send_notification(email_request.owner_email, notification_message)

        return jsonify({"message": "Email scan initiated.", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
