#!/usr/bin/env python3

import praw
import time

def gen_urls_from_sub(sub):
    """Initializes a reddit instance and browses the given sub for urls"""
    reddit = praw.Reddit('meme_browser')
    subreddit = reddit.subreddit(sub)

    for submission in subreddit.hot():
        # Skip selfposts
        if submission.url[-1] == '/':
            continue
        yield submission.url


if __name__ == '__main__':
    print('Testing meme_browser. Generating 1 url per second.')
    for url in gen_urls_from_sub('me_irl'):
        print(url)
        time.sleep(1)
