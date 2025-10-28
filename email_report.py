import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# --- Configuration ---
sender_email = "mk.kappera@gmail.com"
receiver_emails = ["moseskappera@gmail.com", "gayathripadala2804@gmail.com"]  # multiple recipients
password = "guau tyqp ejhx qrop"

# --- Create the email ---
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)
message["Subject"] = "System Health & Error Reports"

# --- Email body ---
body = """\
Hello,

Please find the latest System Health and Error Reports attached.

Regards,
System Monitor
"""
message.attach(MIMEText(body, "plain"))

# --- Attach reports ---
files_to_attach = [
    "/opt/pyscripts/System-monitor/reports/health_report.txt",
    "/opt/pyscripts/System-monitor/reports/monitor.log",
]

for file_path in files_to_attach:
    if os.path.exists(file_path):
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}",
        )
        message.attach(part)
    else:
        print(f" File not found: {file_path}")

# --- Send email ---
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_emails, message.as_string())

print(" Email sent successfully to:", ", ".join(receiver_emails))

