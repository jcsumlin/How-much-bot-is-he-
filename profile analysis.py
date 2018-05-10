# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:52:06 2018

@author: Chat
"""
import praw
import configparser
config = configparser.ConfigParser()
config.read('auth.ini')

reddit = praw.Reddit(client_id=config.get('auth', 'reddit_client_id'),
                     client_secret=config.get('auth', 'reddit_client_secret'),
                     password=config.get('auth', 'reddit_password'),
                     user_agent=config.get('auth', 'reddit_user_agent'),
                     username=config.get('auth', 'reddit_username'))

reddit_user = reddit.redditor('J_C___')
regular_content = 0
bot_content = 0
count = 0
for submission in reddit.redditor('J_C___').submissions.top(limit=1000):
    count += 1
    regular_content += 1
    
for comment in reddit.redditor('J_C___').comments.hot(limit=1000):
    count += 1
    if "I am a script" in comment.body or "Thanks for your original" in comment.body or "[(help me improve!)]" in comment.body or "[Do you have a minute to talk about our lord and savior Stomco?]" in comment.body or "Mirrored post from Instagram" in comment.body:
        bot_content += 1
    else:
        regular_content += 1


print("Percent Bot: %.2f" % (bot_content/(regular_content + bot_content)*100))
users_of_bot = {}
def thanks_bot(users_of_bot):
    subreddit = reddit.subreddit("StarVStheForcesofEvil")
    post_stream = subreddit.comments(limit=1000)
    for comment in post_stream:
        if "!hiatus" in comment.body and comment.author.name not in users_of_bot.keys():
            users_of_bot[comment.author.name] = 1
        elif "!hiatus" in comment.body and comment.author.name in users_of_bot.keys():
            count = users_of_bot.get(comment.author.name)
            users_of_bot[comment.author.name] = count+1
    return users_of_bot

#thanks_bot(users_of_bot)


        