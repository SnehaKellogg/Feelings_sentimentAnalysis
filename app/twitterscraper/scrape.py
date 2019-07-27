import json
import collections
import pandas as pd
import datetime as dt
from query import query_tweets
from query import query_user_info
from ts_logger import logger


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, collections.Iterable):
            return list(obj)
        elif isinstance(obj, dt.datetime):
            return obj.isoformat()
        elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
            return dict(obj)
        elif hasattr(obj, '__dict__'):
            return {member: getattr(obj, member)
                    for member in dir(obj)
                    if not member.startswith('_') and
                    not hasattr(getattr(obj, member), '__call__')}

        return json.JSONEncoder.default(self, obj)

def get(searchterm, model):
#         parser.add_argument("--profiles", action='store_true',
#                             help="Set this flag to if you want to scrape profile info of all the users where you" 
#                             "have previously scraped from. After all of the tweets have been scraped it will start"
#                             "a new process of scraping profile pages.")
#         parser.add_argument("--lang", type=str, default=None,
#                             help="Set this flag if you want to query tweets in \na specific language. You can choose from:\n"
#                                  "en (English)\nar (Arabic)\nbn (Bengali)\n"
#                                  "cs (Czech)\nda (Danish)\nde (German)\nel (Greek)\nes (Spanish)\n"
#                                  "fa (Persian)\nfi (Finnish)\nfil (Filipino)\nfr (French)\n"
#                                  "he (Hebrew)\nhi (Hindi)\nhu (Hungarian)\n"
#                                  "id (Indonesian)\nit (Italian)\nja (Japanese)\n"
#                                  "ko (Korean)\nmsa (Malay)\nnl (Dutch)\n"
#                                  "no (Norwegian)\npl (Polish)\npt (Portuguese)\n"
#                                  "ro (Romanian)\nru (Russian)\nsv (Swedish)\n"
#                                  "th (Thai)\ntr (Turkish)\nuk (Ukranian)\n"
#                                  "ur (Urdu)\nvi (Vietnamese)\n"
#                                  "zh-cn (Chinese Simplified)\n"
#                                  "zh-tw (Chinese Traditional)"
#                                  )
#             if args.profiles and tweets:
#                 list_users = list(set([tweet.user for tweet in tweets]))
#                 list_users_info = [query_user_info(elem) for elem in list_users]
#                 filename = 'userprofiles_' + args.output
#                 with open(filename, "w", encoding="utf-8") as output:
#                     json.dump(list_users_info, output, cls=JSONEncoder)
    tweets = query_tweets(searchterm, limit=10000)
    tweet_dictionary  = (json.dumps(tweets, cls=JSONEncoder))
    tweet_df=pd.read_json(tweet_dictionary)
    smaller_df = tweet_df[["text", "timestamp", "tweet_id", "user_id", "username"]]
    tweet_list = []
    for row in smaller_df.itertuples:
        new_dict= {}
        new_dict['tweet_id'] = row.tweet_id
        new_dict['text'] = row.text
        new_dict['time'] = row.timestamp
        prob_dist = model.prob_classify(row.text)
        new_dict['score'] = prob_dist.prob('pos')
        new_dict['sentiment'] = prob_dist.max()
        #username = row.username
        #twitterscraper.query.quer_user_info
        tweet_list.append(new_dict)

        #username = row.username
        #twitterscraper.query.quer_user_info
        tweet_list.append(new_dict)
    return(tweet_list)

def sentiment_analysis(tweet_list):
    tweet_df=pd.DataFrame(tweet_list)
    average_score = tweet_df["score"].mean()
    total = len(tweet_df.index)
    counts = tweet_df.groupby('sentiment').count()
    if average_score > 0.8:
        sentiment = "Awesome! Over the moon!"
    elif average_score > 0.6:
        sentiment = "Pretty good."
    elif average_score > 0.4:
        sentiment = "Meh. So-So."
    elif average_score > 0.2:
        sentiment = "Dislike"
    else:
        sentiment = "Literally the worst. Active hatred."
    return(average_score, sentiment)
