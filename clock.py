from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week=6)
def run_scrape():
    today = datetime.datetime.today().strftime('%Y-%m-%d')    
    # Word count content file
    wc_content = "wc -l craigslist/craigslist_content.txt"
    # Initialize new links file
    links_command = "touch craigslist/links_" + str(today) + ".txt"
    # Uncomment links pipeline 
    uncomment_links = "sed -i '' '75 s/^#//' craigslist/settings.py"
    # Comment content pipeline
    comment_content = "sed -i '' '76 s/^/#/' craigslist/settings.py"
    # Run links crawl
    links_crawl = "scrapy crawl links"    
    # Comment links
    comment_links = "sed -i '' '75 s/^/#/' craigslist/settings.py"
    # Comment content pipeline
    uncomment_content = "sed -i '' '76 s/^#//' craigslist/settings.py"
    # Run content crawl
    content_crawl = "scrapy crawl content"  
    # Concat content to master 
    concat = "echo craigslist/craigslist_{}.txt >> craigslist/craigslist_content.txt".format(today)

    # Run job
    subprocess.call([wc_content, links_touch, uncomment_links,
                     comment_content, links_crawl, comment_links,
                     uncomment_content, content_crawl, concat,
                     wc_content], shell=True

sched.start()
