from config.config import SERVER_EMAIL_ADRESS, SERVER_EMAIL_PASSWORD
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib 
import re

# Проверка на корректность адреса
def right_email_format(email_adress: str) -> bool:
    right_format_yandex = re.match(r"^[a-zA-Z0-9_.+-]+@yandex.ru", email_adress)
    right_format_google = re.match(r"^[a-zA-Z0-9_.+-]+@gmail.com", email_adress)

    if right_format_yandex or right_format_google:
        return True 
    
    return False


def construct_message(subject="",  text="", img=None, attachment=None):
    msg = MIMEMultipart() 
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    return msg


def send_message(subject: str | None = None, message: str | None = None, receivers: list | None = None):
    smtp = smtplib.SMTP("smtp.yandex.ru", 587) 
    smtp.ehlo() 
    smtp.starttls() 

    smtp.login(SERVER_EMAIL_ADRESS, SERVER_EMAIL_PASSWORD)  

    if None in [subject, message, receivers]:
        return 
    
    approved_receivers = []
    
    for receiver in receivers:
        if right_email_format(receiver):
            approved_receivers.append(receiver)
    
    if not approved_receivers:
        return
    
    msg = construct_message(subject, message) 
    smtp.sendmail(from_addr=SERVER_EMAIL_ADRESS, to_addrs=approved_receivers, msg=msg.as_string()) 
    smtp.quit()
