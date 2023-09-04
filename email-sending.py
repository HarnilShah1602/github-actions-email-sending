import smtplib
import os
from sre_constants import SUCCESS
import ssl

def lambda_handler(event, context):
    port = 465
    smtp_server = "smtp.gmail.com"
    USER_EMAIL = os.environ.get("USER_EMAIL")
    USER_PASSWORD = os.environ.get("USER_PASSWORD")

    message = """\
    Subject: Welcome Harnil

    This is your welcome email running 
    """

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(smtp_server, port, context=context)

    server.login(USER_EMAIL, USER_PASSWORD)
    server.sendmail(USER_EMAIL, USER_EMAIL, message)
    
    return {
        "status": 200,
        "body": SUCCESS
    }



