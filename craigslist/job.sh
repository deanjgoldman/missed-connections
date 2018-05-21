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
echo "Running links crawl"
scrapy crawl links    
# Comment links
sed -i '' '75 s/^/#/' settings.py
# Comment content pipeline
sed -i '' '76 s/^#//' settings.py
# Run content crawl
echo "Running content crawl"
scrapy crawl content 
# Concat content to master 
echo craigslist_${DATE}.txt >> craigslist_content.txt
echo "finished"
