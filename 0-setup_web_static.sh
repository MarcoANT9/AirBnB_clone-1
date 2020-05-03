#!/usr/bin/env bash
# This script sets up a web server for deployment of web_static.

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p data/
mkdir -p data/web_static/
mkdir -p data/web_static/releases/
mkdir -p data/web_static/shared/
mkdir -p data/web_static/releases/test/
echo "Hello Holberton" > data/web_static/releases/test/index.html
ln -sf data/web_static/releases/test/ data/web_static/current
chown -R ubuntu:ubuntu data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    root /usr/share/nginx/html;
        index index.html index.htm;
    server_name localhost;
    location / {
                try_files $uri $uri/ =404;
    }
    location /hbnb_static/ {
    alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default
service nginx restart
