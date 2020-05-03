#!/usr/bin/env bash
# This script sets up a web server for deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# ------------ Create folders if they don't exist ------------------- #

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# ------------ Create fake html file -------------------------------- #
echo "Hello Holberton" > data/web_static/releases/test/index.html

# ------------ Create simbolic link --------------------------------- #

sudo ln -sf data/web_static/releases/test/ data/web_static/current

# ------------ Change ownership of data folder ---------------------- #

sudo chown -R ubuntu:ubuntu data/

# ------------ Configure nginx ---------------------------------------#

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

sudo service nginx restart
