# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open('email_alert') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Anomaly Detected'
msg['From'] = 'detection_team@tempspace.com.au'
msg['To'] = 'd_cull91@hotmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost', 1025)
s.send_message(msg)
s.quit()