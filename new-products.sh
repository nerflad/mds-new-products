#!/bin/bash

curl memphisdrumshop.com/new-products > new-products.html
vim -c "source preprocess.vim" -c "wq" new-products.html
