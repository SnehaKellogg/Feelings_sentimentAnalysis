import json
import collections
import pandas as pd
import datetime as dt
from twitterscraper.query import query_tweets
from twitterscraper.query import query_user_info
from twitterscraper.ts_logger import logger


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

def valid_date(s):
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)

def main(query, begindate, enddate, limit, lang):
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
    tweets = query_tweets(query, begindate, enddate, limit, lang)
    dictionary  = (json.dumps(tweets, cls=JSONEncoder))
    df = pd.read_json(dictionary)
    smaller_df = df[["text", "timestamp", "tweet_id", "user_id", "username"]]
    tweet_list = []
    for row in smaller_df.itertuples():
        new_dict= {}
        new_dict['tweet_id'] = row.tweet_id
        new_dict['text'] = row.text
        new_dict['time'] = row.timestamp
        new_dict['score'] = score
        new_dict['sentiment'] = loaded_model.classify(tweet)
        new_dict['score'] = loaded_model.prob_classify('pos')
        #username = row.username
        #twitterscraper.query.quer_user_info
        tweet_list.append(new_dict)
    return(tweet_list)
