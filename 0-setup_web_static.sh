#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

# mkdir -p means: create the directory and, if required, all parent directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "This is a fake HTML file" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/ a \\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/\;}' /etc/nginx/sites-available/default
sudo service nginx restart
