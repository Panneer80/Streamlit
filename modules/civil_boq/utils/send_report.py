import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_boq_report(html):
    email_sender = "vr80aliens@gmail.com"
    email_receiver = "panneer80@gmail.com"
    subject = "BOQ - Report"
    body = html
    password = st.secrets["smtp_password"]
    try:
            msg = MIMEMultipart("alternative")
            msg['From'] = email_sender
            msg['To'] = email_receiver
            msg['Subject'] = subject
            html_body = MIMEText(html, "html")
            msg.attach(html_body)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_sender, password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
            server.quit()
    except Exception as e:
            print(f"Error sending email : {e}")