import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(args):
    key = os.getenv('API_KEY')
    user_from = args.get("from")
    user_to = args.get("to")
    user_subject = args.get("subject")
    content = args.get("content")

    if not user_from:
        return {"body" : "no user email provided"}
    if not user_to:
        return {"body" : "no receiver email provided"}
    if not user_subject:
        return {"body" : "no subject provided"}
    if not content:
        return {"body" : "no message provided"}
    
    message = Mail(
        from_email = user_from,
        to_emails = user_to,
        subject = user_subject,
        html_content = content)

    sg = SendGridAPIClient(key)
    response = sg.send(message)
    if response.status_code != 202:
        return {"body" : "email failed to send"}