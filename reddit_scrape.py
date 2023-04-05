import requests
import json
import pandas as pd
import datetime

#a function that makes API call to Pushshift API to retrieve the data based on the provided parameters
#https://github.com/pushshift/api
def get_data(subreddit, num_posts, after, before, flair):
    url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size={num_posts}&after={after}&before={before}&flair_text={flair}"
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Error: API request failed with status code {res.status_code}")
        print(f"Response content: {res.content}")
        return None
    try:
        data = json.loads(res.text)
        return data['data']
    except json.JSONDecodeError as e:
        print(f"Error: JSONDecodeError - {e}")
        print(f"Response content: {res.text}")
        return None

#a function that gets all the posts on chunck because the limit of pushshift is 500 per request
def scrape_posts(subreddit, num_posts, after, before, flairs):
    all_posts = []
    for flair in flairs:
        while True:
            posts = get_data(subreddit, num_posts, after, before, flair)
            if not posts:
                break
            all_posts.extend(posts)
            before = posts[-1]['created_utc']
        
    return all_posts

#a function that gets the desired infomation and stores them in a list of dictionaries
def process_posts(posts):
    processed_posts = []
    for post in posts:
        processed_post = {}
        processed_post['id'] = post['id']
        processed_post['text'] = ' '.join(post['selftext'].split()[:200])
        if post["link_flair_text"] in ["Tested Positive - Me", "Presumed Positive"]:
            processed_post['flair'] = post['link_flair_text']
        processed_post['time'] = datetime.datetime.fromtimestamp(post['created_utc'])
        processed_posts.append(processed_post)
    return processed_posts

#the desired parameters
subreddit       = "COVID19Positive" 
flairs          = ["Tested%20Positive%20-%20Me", "Presumed%20Positive"]
num_posts       = 500
after           = 1641044564 #UNIX representation of January 1, 2022
before          = 1680110098 #UNIX representation of March 29, 2023

posts           = scrape_posts(subreddit, num_posts, after, before, flairs)
processed_posts = process_posts(posts)

#Store the information in a dataframe
df = pd.DataFrame(processed_posts)

#more processing to remove undesired rows
df = df[df["flair"].notnull()] #remove rows with null values for flair
df = df[df["text"].notnull()] #remove rows with null values for text
df = df[~df["text"].isin(["[deleted]", "[removed]", ""])] #remove values that has their text as "deleted" or "removed"
df['text'] = df['text'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii')) #remove the non alphabetical characters

#save to csv
df.to_csv("reddit_posts.csv", index=False, encoding='utf-8')

#randomly sample 100 post from each of the two flairs "Tested Positive - Me" and "Presumed Positive"
df_tested_positive   = df[df["flair"] == "Tested Positive - Me"]
df_presumed_positive = df[df["flair"] == "Presumed Positive"]

df_tested_positive_sampled   = df_tested_positive.sample(100)
df_presumed_positive_sampled = df_presumed_positive.sample(100)

data = [df_tested_positive_sampled, df_presumed_positive_sampled]
df_sample = pd.concat(data)

df_sample.to_csv("sampled_postss.csv", index=False)