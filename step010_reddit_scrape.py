
import json
import pandas as pd
import praw
from praw.models import MoreComments
from tqdm import tqdm
import os


from utils import make_and_clear



reddit_config_file = '/home/klybarge/reddit_config.json'
analyses = '/projects/klybarge/covid_diagnosis/analyses'
output_dir = 'step010_reddit_scrape'
destination = os.path.join(analyses, output_dir)



subreddits = [ \
'COVID19positive',
# 'auckland/comments/t0ycbf/what_are_the_first_symptoms_you_noticed_when_you',
# 'UNC/comments/if6rfq/what_are_your_covid_symptoms',
# 'AskReddit/comments/kn5kdo/redditors_who_had_coronavirus_what_was_your',
# 'CoronavirusUS/comments/s10cfj/day_by_day_omicron_symptoms',
# 'Coronavirus/comments/zaqagd/suffering_from_flu_rsv_or_covid19_how_you_can'
    ]

'''
I Think I Have It thread
'''

urls = {}
urls['i_think_i_have_it'] = 'https://www.reddit.com/r/COVID19positive/comments/10cluxp/weekly_i_think_i_have_it_thread_week_of_january/'


target_flair = "Recurring - I Think I Have It"

fields = [ \
    'title',
    'link_flair_text',
    'ups',
    'downs',
    'upvote_ratio',
    'subreddit_name_prefixed',
    'category',
    'content_categories',
    'domain',
    'selftext',
        ]



make_and_clear(destination)

top = 'all'
# top = 500


print('\n'*10)

with open(reddit_config_file, 'r') as f:
    reddit_config = json.load(f)

print('')
for k, v in reddit_config.items():
    print(k, v)




reddit = praw.Reddit(
    client_id=reddit_config["client_id"],
    client_secret=reddit_config["client_secret"],
    user_agent=reddit_config["user_agent"],
)

print('read only:', reddit.read_only)

#assert reddit.user.me() == reddit_config['username'], 'should return usename'
print('user:', reddit.user.me())



for url_name, url in urls.items():
    submission = reddit.submission(url=url)

    print(f'submission:                 "{submission}"')
    for f in fields:
        print(f'{f}:                 "{getattr(submission, f)}"')


# https://medium.com/analytics-vidhya/scraping-reddit-using-python-reddit-api-wrapper-praw-5c275e34a8f4

rows = []
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)

    submissions = subreddit.top(limit=None)
    for i, submission in enumerate(submissions):
        if i < -1:
            print(f'i:                          {i}')
            print(f'submission:                 "{submission}"')
            for f in fields:
                print(f'{f}:                 "{getattr(submission, f)}"')

        row = {}
        for f in fields:
            row[f] = getattr(submission, f)
        rows.append(row)



    submissions = subreddit.search(f"flair_name:{target_flair}", limit=None)
    for i, submission in enumerate(submissions):
        if i < 5:
            print(f'i:                          {i}')
            print(f'submission:                 "{submission}')
            for f in fields:
                print(f'{f}:                 "{getattr(submission, f)}')

        row = {}
        for f in fields:
            row[f] = getattr(submission, f)
        rows.append(row)

    # flair_template = subreddit.flair.link_templates 
    # flair_map = {f['text']:f['id'] for f in flair_template}
    # print(flair_template)
    # # print(flair_map)
    # z = skdlf

    # submissions = subreddit.search('flair:"source code"', syntax='lucene', limit=10)
    # for submission in reddit.subreddit('gamedev').search('flair:"source code"', limit=10):
    #     pass


submission = reddit.submission(url=url)


df = pd.DataFrame(rows)
print(df)

f = os.path.join(destination, 'scrape.csv')

print(f'output file: {f}')
df.to_csv(f)





        # for top_level_comment in submission.comments:
        #     print('-'*80)
        #     if isinstance(top_level_comment, MoreComments):
        #         continue
        #     #print('top_level_comment', top_level_comment)
  
            
        #     # user = top_level_comment.user
        #     body = top_level_comment.body

        #     # print(user)
        #     # print(body)
            


    # # Display the name of the Subreddit
    # print("Display Name:", subreddit.display_name)
    
    # # Display the title of the Subreddit
    # print("Title:", subreddit.title)
    
    # # Display the description of the Subreddit
    # print("Description:", subreddit.description)

    # for top_level_comment in submission.comments[1:]:
    #     if isinstance(top_level_comment, MoreComments):
    #         continue
    #     posts.append(top_level_comment.body)
    # posts = pd.DataFrame(posts,columns=["body"])

    # print(posts)