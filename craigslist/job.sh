#!/bin/bash
# ------------------------------
# jobs for MissedConnections
# ------------------------------

# Enter environment
cd /Users/deangoldman/craigslist/craigslist
source env/bin/activate
# set up environment variables:
# export LOCAL_DATABASE_URL="<LOCAL DATABASE>"
bash setup.sh

# Uncomment links pipeline 
sed -i '' '75 s/^#//' settings.py
# Comment content pipeline
sed -i '' '76 s/^/#/' settings.py
# Run links crawl
echo 'running scrapy links'
scrapy crawl links    
# Comment links
sed -i '' '75 s/^/#/' settings.py
# Comment content pipeline
sed -i '' '76 s/^#//' settings.py
# Run content crawl
echo 'running scrapy content'
scrapy crawl content 
# migrate local db to app env db
heroku pg:reset DATABASE_URL --confirm
heroku pg:push LOCAL_DATABASE_URL
