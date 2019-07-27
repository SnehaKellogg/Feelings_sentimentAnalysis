from kill import tweet_dict
import pandas as pd
import re
from stopwords import stop_words

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)


def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' smile ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' laugh ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' love ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' wink', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' sad ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' cry ', tweet)
    return tweet


def preprocess_tweet(tweet):
    processed_tweet = []
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', 'USER_MENTION', tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    words = tweet.split()

    for word in words:
        word = preprocess_word(word)
        if is_valid_word(word) and word not in stop_words:
            processed_tweet.append(word)

    return ' '.join(processed_tweet)

def get_words(tweet_df):
    words_list_dict=[]
    for row in tweet_df.itertuples():
        new_dict= {}
        new_dict['tweet_id'] = row.tweet_id
        new_dict['text'] = row.text
        cleaned_tweet = preprocess_tweet(row.text)
        new_dict['words']=cleaned_tweet.split()
        new_dict['time'] = row.time
        new_dict['score'] = row.score
        new_dict['sentiment'] = row.sentiment
        words_list_dict.append(new_dict)
    words_list_df=pd.DataFrame(words_list_dict)
    return(words_list_df)

    
def word_breakdown(tweet_sentiment_df):
    words_dict = {}
    for row in tweet_sentiment_df.itertuples():
        score = row.score
        sentiment=row.sentiment
        for word in row.words:
            if word in words_dict.keys():
                words_dict[word]['count'] += 1
                words_dict[word]['score'] = words_dict[word]['score'] + score
            else:
                words_dict[word]={}
                words_dict[word]['count'] = 1
                words_dict[word]['score'] = score
    words_df=pd.DataFrame(words_dict)
    big_words_only=words_df[(words_df.count > 1)]
    return(words_df)

def generate_wordcloud_csv(tweet_dict):
    tweet_df = pd.read_json(tweet_dict)
    full_df = get_words(tweet_df)
    word_df = word_breakdown(full_df)
    word_df=word_df.T
    word_df['average_score']=word_df['score']/word_df['count']
    word_df=word_df[['count', 'average_score']]
    tweet_df.to_csv("data.csv")
    return(tweet_df)
