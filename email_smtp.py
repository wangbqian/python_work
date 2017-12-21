from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


# msg = MIMEText('Hellp send by python ...','plain','utf-8')


# from_addr = input('From : ')
# password = input('Password : ')


# to_addr = input('To : ')

# smtp_server = input('SMTP server: ')

# import smtplib
# server = smtplib.SMTP(smtp_server,587)
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()


#-------- 纯文本邮件 --------#

# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From : ')
# password = input('Password : ')
# to_addr = input('To : ')
# smtp_server = input('SMTP server: ')

# # 邮件对象:
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python测试 <%s>' % from_addr)
# msg['To'] = _format_addr('接受者 <%s>' % to_addr)
# msg['Subject'] = Header('Python 发送邮件测试', 'utf-8').encode()

# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('/Users/fuyiweng/Documents/study/python_work/pillowPg.jpg','rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image','jpeg',filename='text.jpg')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition','attachment',filename='text.jpg')
#     mime.add_header('Content-ID','<0>')
#     mime.add_header('X-Attachment-Id','0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
# import smtplib
# server = smtplib.SMTP(smtp_server,587)
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

#--------- 邮件发送附件 -------------#

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From : ')
password = input('Password : ')
to_addr = input('To : ').split(',')
smtp_server = input('SMTP server: ')

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python测试 <%s>' % from_addr)
msg['To'] = _format_addr('接受者 <%s>' % to_addr)
msg['Subject'] = Header('Python 发送邮件测试', 'utf-8').encode()

# 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/fuyiweng/Documents/study/python_work/pillowPg.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image','jpeg',filename='text.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition','attachment',filename='text.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
    
# 将图片插入到邮件中,这里在发送 HTML 方式中插入图片:
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' + 
        '<p><img src="cid:0"></p>' +
        '</body></html>','html','utf-8'))

import smtplib
server = smtplib.SMTP(smtp_server,587)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

#-------------- 邮件插入图片 ----------#





