
import smtplib
import os

from dotenv import load_dotenv

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

RECIPIENT_DUMMY = 'titorritop@gmail.com'


''' Goal of this project is to use smpplib library to connect to the email server and send the emails.
- We will use .env variables to store credentials
- Files that need to be sent will be under the 'files' dir
- Finally, we will autometate the script 
- Erros will be under teh 'project2/logs' dir

'''


def init():
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return email, password


email, password = init()


def mail_server(email, password):
    email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    email_server.starttls()
    email_server.login(email, password)
    return email_server


print(email)
print(password)
