"""wang

这个会有点高级
"""
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = MIMEMultipart()

email["From"] = "3538384775@qq.com"
email["To"]="2381662434@qq.com"
email["Subject"] = Header("加油呀,严rr","utf-8")
content = """sorry"""
email.attach(MIMEText(content,"plain","utf-8"))

smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtp_obj.login('3538384775@qq.com', 'snrgkecgxcohdbda')
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    '3538384775@qq.com',
    ["2381662434@qq.com"],
    email.as_string()
)

