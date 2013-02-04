#!/usr/bin/env python

import pickle
import feedparser
import os
import sys
<<<<<<< HEAD

from sh import chromium

CACHE_FILE = os.getenv('HOME') + '/.last_entries'
RSS_FILE = os.getenv('HOME') + '/rss_urls'

def main():
    try:
        with open(CACHE_FILE, 'rb') as last_entries_file:
            last_entries = pickle.load(last_entries_file)
    except (FileNotFoundError, OSError):
=======
from sh import chromium

if __name__ == '__main__':
    
    CACHE_FILE = os.getenv('HOME') + '/.last_entries'
    RSS_FILE = os.getenv('HOME') + '/rss_urls'
    
    rss_urls =[]
    
    
    try:
        with open(CACHE_FILE, 'rb') as last_entries_file:
            last_entries = pickle.load(last_entries_file)
    except FileNotFoundError:
>>>>>>> 758c15fe26baf9b9bc150e10147b82a7b0f98b29
        last_entries = []
       
    new_entries = []
    
    try:
        with open(RSS_FILE) as rss_file:
            rss_urls = rss_file.read().split()
    except FileNotFoundError:
        print('The configuration file with feed urls is missing, fix it!')
        sys.exit(1)

    for url in rss_urls:
        parsed = feedparser.parse(url)
        for entry in parsed.entries:
            if entry not in last_entries:
                chromium(entry.link)
                print('Opened {}'.format(entry.link))
            new_entries.extend(parsed.entries)
    
    with open(CACHE_FILE, 'wb') as last_entries_file:
        pickle.dump(new_entries, last_entries_file)
<<<<<<< HEAD

if __name__ == '__main__':
    main()
=======
>>>>>>> 758c15fe26baf9b9bc150e10147b82a7b0f98b29
