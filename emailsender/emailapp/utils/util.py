import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user_email, receiver_email, subject, text, server):
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain'))

    server.send_message(msg)

def sendEmail(user_email, password, subject, text, csv_file):
    # Define the SMTP servers and ports for different email providers
    email_providers = {
        'gmail.com': {'server': 'smtp.gmail.com', 'port': 587},
        'outlook.com': {'server': 'smtp-mail.outlook.com', 'port': 587},
        'yahoo.com': {'server': 'smtp.mail.yahoo.com', 'port': 587},
        'aol.com': {'server': 'smtp.aol.com', 'port': 587},
        'hotmail.com': {'server': 'smtp.live.com', 'port': 587},
        'protonmail.com': {'server': 'smtp.protonmail.com', 'port': 587}
    }

    # Get the email domain from the user email
    email_domain = user_email.split('@')[1]

    # Get the SMTP server and port for the email domain
    smtp_server = email_providers[email_domain]['server']
    smtp_port = email_providers[email_domain]['port']

    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(user_email, password)

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # get the header row

        # Find the index of the column that contains email addresses
        email_index = header.index('email')  # replace 'email' with the exact header name for the email column

        emails = []
        for row in reader:
            receiver_email = row[email_index]

            if receiver_email:
                emails.append(receiver_email)

        for receiver_email in emails:
            send_email(user_email, receiver_email, subject, text, smtp)

    smtp.quit()
