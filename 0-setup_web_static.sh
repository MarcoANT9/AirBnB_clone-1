#!/usr/bin/env bash
# This script sets up a web server for deployment of web_static.

if ! which nginx > /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
    ufw allow 'Nginx HTTP'
fi

# ------------ Create folders if they don't exist ------------------- #

mkdir -p data/
mkdir -p data/web_static/
mkdir -p data/web_static/releases/
mkdir -p data/web_static/shared/
mkdir -p data/web_static/releases/test/

# ------------ Create fake html file -------------------------------- #
echo -ne "<html>\n<head>\n</head>\n<body>\ntHolberton School\n</body>\n</html>\n" > data/web_static/releases/test/index.html

# ------------ Create simbolic link --------------------------------- #

ln -s -f data/web_static/releases/test/ data/web_static/current

# ------------ Change ownership of data folder ---------------------- #

chown -R ubuntu:ubuntu data/

# ------------ Configure nginx ---------------------------------------#

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=sCNrK-n68CM;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

}" > /etc/nginx/sites-available/default

service nginx restart
