#!/usr/bin/env python3

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from smtplib import SMTP
import datetime
import os
import sys
import urllib.request

def bs4_resultset_to_strings(list_):
    for i,x in enumerate(list_):
        list_[i] = "".join((str(x), '\n'))
    return list_

def time_string():
    return str(datetime.datetime.now())[:19]

def get_credentials():
    try:
        with open('credentials', 'r') as _file:
            _lines = [str(i).strip('\n') for i in _file]
    except EnvironmentError:
        print(time_string(), ':\tcredentials not found', sep='')
        quit(1)
    return _lines

def get_email_list():
    try:
        with open('email-list', 'r') as _file:
            recipients = [i.strip('\n') for i in _file]
    except EnvironmentError:
        print(time_string(), ':\temail-list not found', sep='')
        quit(1)
    return recipients


# ------------------------------------------------------------------------------
#       check for new products
# ------------------------------------------------------------------------------
if os.path.isfile('items.html'):
    with open('items.html', 'r') as _file:
        stale_soup = BeautifulSoup(_file.read(None), 'html.parser')
    stale_items = bs4_resultset_to_strings(stale_soup.find_all('li', class_='item'))
else:
    stale_items = []

page = urllib.request.urlopen("http://memphisdrumshop.com/new-products").read()
page = page.decode("utf-8")
soup = BeautifulSoup(page, 'html.parser')
items = bs4_resultset_to_strings(soup.find_all('li', class_='item'))

# update items.html, don't bother if the items are exactly the same
if not stale_items == items:
    with open('items.html', 'w+') as _file:
        for i in items:
            _file.write(i)
    print(time_string(), ':\tUpdated items.html.', sep='')

new_items = [x for x in items if x not in stale_items]

if not new_items:
    print(time_string(), ':\tNo new products.', sep='')
    quit(0)


# ------------------------------------------------------------------------------
#       send emails (if we need to)
# ------------------------------------------------------------------------------
with open('header.html', 'r') as _file:
    header = [str(i) for i in _file]

email_body = header + new_items + ['\n</ol>', '\n</body>', '\n</html>']
email_body = ''.join(email_body)

credentials = get_credentials()
server = credentials[0]
port = credentials[1]
username = credentials[2]
password = credentials[3]

with SMTP(server, port) as session:
    session.ehlo()
    session.starttls()
    session.login(username, password)

    for message_to in get_email_list():
        msg = MIMEText(email_body, 'html')
        msg['To'] = message_to
        msg['From'] = username
        msg['Subject'] = 'MyCymbal Digest: New Products'
        msg = msg.as_string()
        session.sendmail(username, message_to, msg)
        print(time_string(), ':\tEmailed ', message_to, sep='')
