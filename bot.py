import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


bot that follows back named users, or followers based on followers count
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    #print(follower.name)           #giving us the list of followers
    # if follower.name == 'followernameontwitter':
    #     follower.follow()
    #     break
    if follower.followers_count > 1000:
        follower.follow()
        break

# bot that follows or likes based on a used term
search_string = '#100DaysOfCode'
numberOfTweets = 100

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
        try:
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break







