#!/bin/bash

fetchPage() {
    curl -s -S -A "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0" \
        memphisdrumshop.com/new-products > new-products.html;
    vim -E -c "source preprocess.vim" -c "wq" new-products.html > /dev/null;
}


if [ -e new-products.html ]; then
   mv new-products.html new-products.html.old;
   fetchPage;
   diff new-products.html new-products.html.old && nothingNew=1
   rm new-products.html.old
else
    fetchPage;
fi

if [[ $nothingNew -eq 1 ]]; then
    echo No new products.
    exit 0
else
    for i in $(< email_list); do
        ./send-email.py $i
    done
fi
