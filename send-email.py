#!/usr/bin/python

import os
import sys
import smtplib
from email.mime.text import MIMEText

recipients = []

with open('credentials', 'r') as _file:
    _lines = [str(e).strip('\n') for e in _file]
    server = _lines[0]
    port = _lines[1]
    username = _lines[2]
    password = _lines[3]

with open('new-products.html', 'r') as _file:
    _message = _file.read()

with open('email_list', 'r') as _file:
    recipients = [e.strip('\n') for e in _file]


session=smtplib.SMTP(server, port)
session.ehlo()
session.starttls()
session.login(username, password)

for message_to in recipients:
    msg = MIMEText(_message, 'html')
    msg['To'] = message_to
    msg['From'] = username
    msg['Subject'] = 'ALERT: New Cymbals detected on mycymbal.com'
    msg = msg.as_string()
    session.sendmail(username, message_to, msg)
    print('Emailed', message_to)

session.quit()
