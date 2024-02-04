
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def auth_gmail():
    json_config_file = 'gmail_set_up.json'
    return json_config_file

sender_email = 'vctrubio@gmail.com'
recipient_email = 'titorritop@gmail.com'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Subject of the Email'

body = 'This is the body of the email.'
message.attach(MIMEText(body, 'plain'))

flow = InstalledAppFlow.from_client_secrets_file(auth_gmail(), ['https://mail.google.com/'])
credentials = flow.run_local_server()

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(user=sender_email, password=credentials.token)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

# The email has been sent successfully
print("Email sent successfully!")

