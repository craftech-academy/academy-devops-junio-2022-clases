#!/bin/ash

while true; do
    curl -t 1 ${NGINX_IP} > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "$(date +"%s") - [INFO] Connection to Nginx working :)"
    else
        echo "$(date +"%s") - [ERROR] Connection to Nginx failed"
    fi
    sleep 2
done