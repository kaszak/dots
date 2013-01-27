#!/usr/bin/env python

import pickle
import feedparser
import os
import re
import sys
from datetime import datetime
from sh import chromium, sleep

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

date_pclab = re.compile(r'''
    ^
    \D{3},\   #Match Day, grouping it is not necessary, ex: Tue,
    (\d{,2})\ #Match numerical value of Day
    (\D{3})\  #Match Month, ex: Dec
    (\d{4})\  #Match Year, four digits
    (\d{2}):  #Hours
    (\d{2}):  #Minutes
    (\d{2})   #Seconds
    $
    ''', re.VERBOSE)

def PclabHandler(DateString):
    """parse a UTC date in DDD, DD MMM YYYY HH:MM:SS"""
    try:
        day, month, year, hour, minute, second = date_pclab.search(DateString).groups()
        #parsed_date = list(date_pclab.search(DateString).groups())
    except AttributeError:
        return None
    month = months.index(month) + 1
    #return parsed_date
    return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)).timetuple()
    #return datetime(*parsed_date).timetuple()

if __name__ == '__main__':
    
    TIME_FILE = os.getenv('HOME') + '/.last_time'
    RSS_FILE = os.getenv('HOME') + '/rss_urls'
    
    rss_urls =[]
    
    
    try:
        with open(TIME_FILE, 'rb') as time_file:
            last_time = pickle.load(time_file)
    except FileNotFoundError:
        last_time = datetime.today().timetuple()
        with open(TIME_FILE, 'wb') as time_file:
            pickle.dump(datetime.today().timetuple(), time_file)
        print('Saved current time as last_time.')
        sys.exit()
    
    try:
        with open(RSS_FILE) as rss_file:
            for line in rss_file:
                rss_urls.append(line.strip())
    except FileNotFoundError:
        print('The configuration file with feed urls is missing, fix it!')
        sys.exit(1)

    feedparser.registerDateHandler(PclabHandler)
    for url in rss_urls:
        parsed = feedparser.parse(url)
        for entry in parsed.entries:
            if entry.published_parsed > last_time:
                chromium(entry.link)
                print('Opened {}'.format(entry.link))
    
    with open(TIME_FILE, 'wb') as time_file:
        pickle.dump(datetime.today().timetuple(), time_file)
