# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

user = 'enter email here'
gpass = 'enter password here'
try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(user, gpass)
    # Open the plain text file whose name is in text file for reading.
    with open('email_alert') as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Anomaly Detected'
    msg['From'] = user
    msg['To'] = 'chrisbreed01@gmail.com'

    server_ssl.send_message(msg)
    server_ssl.quit()
    print('message sent')

except:
    print('Something went wrong...')