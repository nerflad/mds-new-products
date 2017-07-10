#!/usr/bin/python

import os
import sys
import smtplib
from email.mime.text import MIMEText

if len(sys.argv) < 2:
    print('USAGE: ', os.path.basename(__file__), '<recipient@example.com>')
    quit(1)
else:
    message_to = str(sys.argv[1])

with open('credentials', 'r') as _file:
    username = str(_file.readline())
    password = str(_file.readline())

with open('new-products.html', 'r') as _file:
    _message = _file.read()

msg = MIMEText(_message, 'html')
msg['To'] = message_to
msg['From'] = username
msg['Subject'] = 'ALERT: New Cymbals detected on mycymbal.com'
msg = msg.as_string()

session=smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(username, password)
session.sendmail(username, message_to, msg)
session.quit()

print('Emailed ', message_to, '.')
