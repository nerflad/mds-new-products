#!/bin/bash

# change to project directory, in case the script is being run by cron or something
cd "${0%/*}"

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
    echo -e $(date +%x_%H:%M:%S:%N | sed 's/...$//'):\t No new products.
    exit 0
else
    ./send-email.py
fi
