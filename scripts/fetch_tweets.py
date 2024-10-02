# import tweepy
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from config import TWITTER_API_KEYS

# def get_twitter_client():
#     auth = tweepy.OAuthHandler(
#         TWITTER_API_KEYS["API_KEY"], 
#         TWITTER_API_KEYS["API_SECRET"]
#     )
#     auth.set_access_token(
#         TWITTER_API_KEYS["ACCESS_TOKEN"], 
#         TWITTER_API_KEYS["ACCESS_SECRET"]
#     )
#     return tweepy.API(auth)

# def get_user_tweets(username, count=10):
#     client = get_twitter_client()
#     try:
#         tweets = client.user_timeline(screen_name=username, count=count, tweet_mode="extended")
#         return [{'text': tweet.full_text, 'created_at': str(tweet.created_at)} for tweet in tweets]
#     except tweepy.errors.TweepyException as e:  # Use tweepy.errors.TweepyException for Tweepy 4.x.x
#         raise Exception(f"Error fetching tweets: {str(e)}")
    
import tweepy
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import TWITTER_API_CONFIG

def get_twitter_client():
    client = tweepy.Client(bearer_token=TWITTER_API_CONFIG["BEARER_TOKEN"])
    return client

def get_user_tweets(username, max_results=10):
    client = get_twitter_client()
    try:
        # First, get the user ID
        user = client.get_user(username=username)
        if not user.data:
            raise Exception(f"User {username} not found")
        
        user_id = user.data.id
        
        # Then get their tweets
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=max_results,
            tweet_fields=['created_at', 'text']
        )
        
        if not tweets.data:
            return []
        
        return [
            {
                'text': tweet.text,
                'created_at': str(tweet.created_at)
            }
            for tweet in tweets.data
        ]
    except Exception as e:
        raise Exception(f"Error fetching tweets: {str(e)}")



# import tweepy
# import logging
# from config import TWITTER_API_BEARER_TOKEN

# # Setup logger
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()

# # Create a Tweepy client using the Bearer Token
# client = tweepy.Client(bearer_token=TWITTER_API_BEARER_TOKEN)

# def get_tweets(username):
#     try:
#         # Fetch the user by username
#         user = client.get_user(username=username)
#         user_id = user.data['id']

#         # Fetch tweets
#         response = client.get_users_tweets(id=user_id, max_results=10, tweet_fields=['text'])
#         tweets = response.data

#         if not tweets:
#             logger.warning(f"No tweets found for user {username}")
#             return None

#         return [{'text': tweet['text']} for tweet in tweets]

#     except tweepy.errors.Forbidden as e:
#         logger.error(f"Error fetching tweets: {e}")
#         return None
#     except Exception as e:
#         logger.error(f"Unexpected error occurred: {e}")
#         return None
