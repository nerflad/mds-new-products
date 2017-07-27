#!/bin/bash

# change to project directory to satisfy the cron gods
cd "${0%/*}"

# trim log if need be (1024 lines ought to be enough)
if [ -e mds-cron.log ] && [ $(wc -l mds-cron.log | awk '{print $1}') -gt 1024 ]; then
    truncatedlog=$(tail -n 1024 mds-cron.log) && echo "${truncatedlog}" > mds-cron.log && \
    echo -e $(date +%x\ %H:%M:%S):\t Truncated mds-cron.log to 1024 lines. >> mds-cron.log
fi

./mds-new-products.py >> mds-cron.log
