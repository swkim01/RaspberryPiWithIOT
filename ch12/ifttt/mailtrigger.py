#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
from email.header import Header
import os

smtp_server = "smtp.gmail.com"
port = 587
portssl = 465
userid = "mymail@gmail.com"
passwd = "password"
recvid = "trigger@recipe.ifttt.com"

def sendmail(from_user, to_user, cc_users, subject, text, attach):
    COMMASPACE = ", "
    msg = MIMEMultipart("alternative")
    msg["From"] = from_user
    msg["To"] = to_user
    msg["Co"] = COMMASPACE.join(cc_users)
    msg["Subject"] = Header(s=subject, charset="utf-8")

    if(text != None):
        msg.attach(MIMEText(text))

    if(attach != None):
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(attach, "rb").read())
        Encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(attach))
        msg.attach(part)

    server = smtplib.SMTP(smtp_server, port)
    #server = smtplib.SMTP_SSL(smtp_server, portssl)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    ret, m = server.login(userid, passwd)
    if ret != 235:
        print "login fail"
        return
    server.sendmail(from_user, to_user, msg.as_string())
    server.quit()

if __name__ == "__main__":
    sendmail(userid, recvid, "", "Test", "This is test mail!", None)
