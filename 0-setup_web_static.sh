#!/usr/bin/env bash
# Sets up a web servers for deployment of web_static.
sudo apt-get update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/releases/test /data/web_static/shared/
fake_file=/data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n<\html>" | sudo tee $fake_file
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
config_file=/etc/nginx/sites-available/default
sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file
service nginx restart
