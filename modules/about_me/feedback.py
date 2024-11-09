import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Taking inputs
st.markdown("##### Feedback Form")
st.divider()
email_sender = "vr80aliens@gmail.com"
email_receiver = "panneer80@gmail.com"
subject = "BOQ - Feedback"
body = st.text_area('Your feedback helps me improve and bring you the content you want to see.')
password = st.secrets["smtp_password"]

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Erreur lors de l’envoi de l’e-mail : {e}")