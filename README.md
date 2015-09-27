# SWIFT Static Site
https://calpolyswift.org

Suggested IDE is PyCharm.

## Requirements
python 2.7

python-flask

libapache2-mod-wsgi

## Deployment Instructions
Simlink from sites-enabled to the VirtualHost file included.

## Update Instructions
Until a github webhook is added just: 

cd /srv/http/SWIFT-Static-Site

git pull

## Production Warnings
Set debug=false in production.

Make sure to have all files UTF-8 encoding. Flask can not handle other encodings.

Must be named SWIFT_Static_Site.py, '-' leads to syntax error in python. 