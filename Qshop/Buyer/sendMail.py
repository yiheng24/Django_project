import smtplib
from email.mime.text import MIMEText


subject='练习发送软件'

content='我是邮件的内容。。。。内容1234567'

sender='yi8heng24@163.com'

recver='yiheng24@qq.com,576492000@qq.com'

password='576492yh'

message=MIMEText(content,'plain','utf-8')

message['Subject']=subject

message['From']=sender

message['To']=recver

smtp=smtplib.SMTP_SSL('smtp.163.com',465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(','),message.as_string())
smtp.close()