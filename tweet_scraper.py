import snscrape.modules.twitter as sntwitter

def get_tweet_text(tweet_url: str) -> str:
    tweet_id = tweet_url.strip().split("/")[-1]
    for tweet in sntwitter.TwitterTweetScraper(tweet_id).get_items():
        return tweet.content
    return ""
