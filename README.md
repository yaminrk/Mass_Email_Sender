# Mass_Email_Sender
## Overview
This is a web application that allows you to send emails to multiple recipients at once. It reads the recipient email addresses from a CSV file and sends an email to each one. The application supports multiple email providers.

## Prerequisites
- A modern web browser (Chrome, Firefox, Safari, etc.)
- A CSV file with a column named 'email' containing the email addresses of the recipients

## Libraries Used
- csv
- smtplib
- email.mime.multipart
- email.mime.text

## How to Use
1. Open the web application in your browser.
2. Fill in the form fields with your email address, password, subject, and text.
3. Upload your CSV file.
4. Click the "Submit" button to send the emails.

## Functionality
The web application uses a Python script on the backend to send the emails. When you submit the form, the script logs into the SMTP server with the provided email address and password. It then reads the CSV file and extracts the email addresses. For each email address, it creates a new email with the provided subject and text, and sends it using the SMTP server.

The script automatically selects the SMTP server and port based on the email domain. It currently supports Gmail, Outlook, Yahoo, AOL, Hotmail, and ProtonMail. You can easily add more email providers by updating the `email_providers` dictionary in the script.

## Note
Different email providers may have different security settings. For example, to use Gmail's SMTP server, you may need to enable "Less secure app access" in your Google account settings.

