import smtplib
import os
from email.message import EmailMessage

sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")
receiver_email = input("Enter receiver email: ")

message = EmailMessage()
message["Subject"] = "Test Email"
message["From"] = sender_email
message["To"] = receiver_email

message.set_content("Hello! This is a test email sent using Python.")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)

    print("Email sent successfully.")

except Exception as e:
    print("Error:", e)