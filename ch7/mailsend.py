#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email import Utils
from email.header import Header
import os

smtp_server = "smtp.gmail.com"
port = 587
portssl = 465
userid = "mymail@gmail.com"
recvid = "yourmail@gmail.com"
passwd = "password"

def send_mail(from_user, to_user, cc_users, subject, text, attach):
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

    smtp = smtplib.SMTP_SSL(smtp_server, portssl)
    #smtp = smtplib.SMTP(smtp_server, port)
    smtp.ehlo()
    #smtp.starttls()
    smtp.login(userid, passwd)
    smtp.sendmail(from_user, to_user, msg.as_string())
    smtp.close()

send_mail(userid, recvid, "", "capture", "view file", "capture.jpg")

