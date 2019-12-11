import tweepy
import schedule
import time


# Program sends a tweet once every minute

# Counter used to number each tweet that is posted
global i
i = 0

'''
Contains access keys and sends tweet
CONSUMER/ACCESS Keys are accessed from the twitter API/Developer App
'''
def code():
    i += 1
    # Authenticate/Grant access to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status("This tweet was created with a bot - test " + str(i))

# scheduled tweet
schedule.every(1).minutes.do(code)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
