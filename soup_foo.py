#!/usr/bin/env python3

from bs4 import BeautifulSoup

with open('foo-products.html', 'r') as _file:
    html_doc = _file.read(None)

soup = BeautifulSoup(html_doc, 'html.parser')


