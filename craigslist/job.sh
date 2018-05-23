#!/bin/bash

# Uncomment links pipeline 
sed -i '' '75 s/^#//' settings.py
# Comment content pipeline
sed -i '' '76 s/^/#/' settings.py
# Run links crawl
scrapy crawl links    
# Comment links
sed -i '' '75 s/^/#/' settings.py
# Comment content pipeline
sed -i '' '76 s/^#//' settings.py
# Run content crawl
scrapy crawl content 

# Add to github
#git add logfile.txt
#git commit -m "update ${DATE}"
#git pull origin master
#git push origin master
#git push heroku master
