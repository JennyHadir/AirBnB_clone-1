#!/usr/bin/env bash
# prepare a web server
# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# Create some folders if it doesn't exist
sudo mkdir -p /data/web_static/realeses/test
sudo mkdir -p /data/web_static/shared
# Create a fake html file
echo "Hello holberton" >> sudo tee /data/web_static/realeses/test/index.html
# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership
sudo chown -hR ubuntu:ubuntu /data
# Update nginx config
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart nginx
sudo service nginx restart