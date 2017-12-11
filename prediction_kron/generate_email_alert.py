# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

user = 'anomalydetection9@gmail.com'
gpass = 'l23BXNQoDG7I'


def send_email(message):
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(user, gpass)
        msg = EmailMessage()
        msg.set_content(message)

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'Anomaly Detected'
        msg['From'] = user
        msg['To'] = 'd_cull91@hotmail.com'

        server_ssl.send_message(msg)
        server_ssl.quit()
        print('message sent')

    except:
        print('Something went wrong...')