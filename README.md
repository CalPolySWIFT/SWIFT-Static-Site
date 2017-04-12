# SWIFT Static Site
https://calpolyswift.org

Suggested IDE is PyCharm.

## Requirements
python 2.7

python-flask

libapache2-mod-wsgi

## Development Warnings
When using PyCharm the working directory option must be set to the root of the project, otherwise everything is just 404.

## Deployment Instructions
Simlink from sites-enabled to the VirtualHost file included.

## Update Instructions
Webhook should automatically restart the container and fetch the latest files.

~~Until a github webhook is added just:~~\
~~cd /srv/http/SWIFT-Static-Site~~\
~~git pull~~

### Docker
Docker image can be updated with `docker-compose restart swift-static-site`. Image internally uses git on boot to update.

## Production Warnings
Set debug=false in production.

Make sure to have all files UTF-8 encoding. Flask can not handle other encodings.

Must be named SWIFT_Static_Site.py, '-' leads to syntax error in python. 
