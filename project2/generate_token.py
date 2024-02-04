from google.auth.transport.requests import Request
from google.oauth2 import service_account

def create_app_password(credentials_file, email, scope):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=[scope]
    )
    credentials.refresh(Request())

    # Extract the access token
    access_token = credentials.token

    # Print the access token (for demonstration purposes)
    print(f'Access Token: {access_token}')

# Replace 'path/to/your/credentials.json' with the path to your service account JSON key file
credentials_file = 'gmail_set_up.json'

# Replace 'your_email@gmail.com' with your Gmail address
email = 'vctrubio@gmail.com'

# The scope for Gmail API
gmail_scope = 'https://www.googleapis.com/auth/gmail.settings.basic'

create_app_password(credentials_file, email, gmail_scope)
