#!/usr/bin/env python3

import os
import praw
import time
import urllib

sub = 'me_irl'

def gen_urls_from_sub(sub):
    """Initializes a reddit instance and browses the given sub for urls"""
    reddit = praw.Reddit('meme_browser')
    subreddit = reddit.subreddit(sub)

    for submission in subreddit.hot(limit=200):
        # Skip selfposts
        if submission.url[-4:] != '.jpg':
            continue
        yield submission.url


if __name__ == '__main__':
    print("Content-Type: text/html")
    print("""
        <html>
        <body>
        <p>print test</p>
        </body>
        </html>
    """)
    for url in gen_urls_from_sub(sub):
        print("""
            <html>
                <body>
                    <p> generating meme: """+url+""" <p>
                </body>
            </html>
        """)
        urllib.request.urlretrieve(str(url), 'media/meme.jpg')
        time.sleep(15)
