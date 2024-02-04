
import smtplib
import os

from dotenv import load_dotenv

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

RECIPIENT_DUMMY = 'titorritop@gmail.com'


def init():
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return email, password



def mail_server(email, password):
    email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    email_server.starttls()
    email_server.login(email, password)
    return email_server

def mimme_email():
    pass



email, password = init()

i = mail_server(email, password)
# print(i)