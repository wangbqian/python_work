#-*- coding: utf-8 -*-
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr



# 输入邮件地址, 口令和POP3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

server = poplib.POP3_SSL(pop3_server,995)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)


# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp,mails,octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)


index = len(mails)
resp,lines,cotets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

server.quit()

#--------------   解析邮件



# msg = Parser().parsestr(msg_content)


def decode_str(s):
    value,charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type','').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
        return charset




# indent用于缩进显示:
def print_info(msg,indent=0):
    if indent == 0:
        for header in ['From','To','Subject']:
            value = msg.get(header,'')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr,addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' %(name,addr)
            print('%s%s: %s' % (' ' * indent,header,value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n,part in enumerate(parts):
            print('%spart %s' %(' ' * indent,n))
            print('%s-----------------' %(' ' * indent))
            print_info(part,indent +1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' %(' ' * indent,content + '....'))
        else:
            print('%sSttachment: %s ' % (' ' * indent,content_type))




print_info(msg)






