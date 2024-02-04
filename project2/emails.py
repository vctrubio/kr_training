'''
This is just the script.
Please find the complete project in:
        https://github.com/vctrubio/kr_training/tree/main/project2
'''

import os
import smtplib
import schedule
import time

from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

SMTP_SERVER = 'smtp.mail.yahoo.com'
SMTP_PORT = 587


def init():
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    return email, password

    
def recipients_list():
    with open('files/recipient.txt', 'r') as file:
        return [line.strip() for line in file]


def debug_print(*args):
    print(args)


def mail_server(email, password):
    try:
        email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        email_server.starttls()
        email_server.login(email, password)
        print('Email server connected successfully')
        return email_server
    except Exception as e:
        print(f'Error: {e}')
        return None


def create_mail(email, send_to, subject, body):
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = send_to
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    return message


def iterate_report():
    path = 'files/reports/'
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.reverse()
    
    for i in files:
        with open(os.path.join(path, i), 'r') as file:
            context = file.read()
            send_mail(context)


def send_mail(context):
    global email, email_server, recipients
    if not email_server:
        print('BIG ERROR in email server')
        exit(101)
        
    try:
        for recipient in recipients:
            message = create_mail(email, recipient, 'Automated Email', context)
            email_server.sendmail(email, recipient, message.as_string())
            print(f'Email sent to {recipient}')
    except Exception as e:
        print(f'Mail Error: {e}')
    finally:
        email_server.quit()
    print('Email server completed')


print('init schedule...')

email, password = init()
email_server = mail_server(email, password)
recipients = recipients_list()


schedule.every().day.at("12:00").do(iterate_report)

while True:
    schedule.run_pending()
    time.sleep(1)