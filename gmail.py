from Google import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
CLIENT_SECRET_FILE='client_secret.json'
API_NAME='samadhaan'
API_VERSION='v1'
SCOPES=('https://mail.google.com')
service=create_service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
