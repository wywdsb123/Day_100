"""wang

先看看
"""
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

from rich.jupyter import display

from email2 import attachment

EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 465
EMAIL_USER = "3538384775@qq.com"
EMAIL_AUTH = "snrgkecgxcohdbda"

def send_email(*,from_user,to_users,subject="",content="",filenames=[]):
    email = MIMEMultipart()
    email["From"] = from_user
    email['To'] = to_users
    email['Subject'] = subject

    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open (filename,"rb") as file :
            pos = filename.rfine("/")
            display_filename = filename[pos+1:] if pos>=0 else filename
            display_filename =quote(display_filename)
            attachment = MIMEText(file.read(),"base64","utf-8")
            attachment["content-type"] = f'attachment;filename = "{display_filename}"'
            email.attach(attachment)
    smtp = smtplib.SMTP_SSL(EMAIL_HOST,EMAIL_PORT)
    smtp.login(EMAIL_USER,EMAIL_AUTH)
    smtp.sendmail(from_user,to_users.split(","),email.as_string())

