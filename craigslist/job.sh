#!/bin/bash

# Today's date
DATE=$(date +%Y-%m-%d)
# word count content
wc -l craigslist_content.txt
# initialize new file
touch links_${DATE}.txt
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
# Concat content to master 
echo craigslist_${DATE}.txt >> craigslist_content.txt
# Remove duplicates from craigslist_content.txt
sed -i '' 'g/\v%(^\1\n)@<=(.*)$/d' craigslist_content.txt
# Logfile
wc -l craigslist_content_${DATE}.txt >> logfile.txt
# Add to github
git add craigslist_content.txt
git add logfile.txt
git commit -m "update ${DATE}"
git pull origin master
git push origin master
git push heroku master


