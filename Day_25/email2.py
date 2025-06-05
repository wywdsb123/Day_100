"""wang

发送带有附件的邮件
"""
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

email = MIMEMultipart()

email["From"] = "3538384775@qq.com"
email["To"] = "2381662434@qq.com"
email["Subject"] = Header("请查收退学通知书","utf-8")

content="""<p>亲爱的言同学:</p>
<br><p>祝,好!</p><hr><p>严同学 即日</p>"""
email.attach(MIMEText(content,"html","utf-8"))
with open("水印.docx","rb") as file :
    attachment =MIMEText(file.read(),"base64","utf-8")
    attachment['content-type'] = 'application/octet-stream'
    filename = quote("严同学退学报告.docx")
    attachment['content-disposition'] = f'attachment; filename="{filename}"'
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com",465)
smtp_obj.login("3538384775@qq.com","snrgkecgxcohdbda")
smtp_obj.sendmail("3538384775@qq.com",
    "2381662434@qq.com",
                  email.as_string()
                  )
