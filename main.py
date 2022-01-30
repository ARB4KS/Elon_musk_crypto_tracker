import tweepy
import datetime
import re
import pandas


time = datetime.datetime.utcnow()

data = pandas.read_csv("CRYPTONAMES.csv")
ban = pandas.read_csv("BAN_WORDS.csv")
ban_words = ban.BAN_WORDS.to_list()
print(ban_words)
cryptonames = data.CRYPTO_NAME.to_list()
cryptoabbreviation = data.ABBREVIATION.to_list()

print(cryptonames)
print(cryptoabbreviation)
print()


def formathour(hour):

    time_format = hour.isoformat()
    strtime_format = str(time_format)
    final_hour = re.split('[: T -]', strtime_format)
    return final_hour
actual_hour = formathour(time)
print(actual_hour)

def checkhour(currenthour, tweethour):
    for loop in range(5):
        if currenthour[loop] != tweethour[loop]:
            return False

    return True


def crypto_name_check():
    buy = False
    crypto = ""
    for loop in tweet_words:
        if loop in ban_words:
            return crypto

    for loop in tweet_words:
        if loop in cryptoabbreviation:
            return loop
        if loop in cryptonames:
            get_index = data[data.CRYPTO_NAME == loop]
            get_abbreviation = get_index.ABBREVIATION
            abbreviation =get_abbreviation.to_string(index=False, header=False)
            print(abbreviation)
            return abbreviation


api_key2 = "rbHMprgPldsOji5xzz1fKj0RR"

api_key_secret2 = "3hKyVTIsTBAWymByOFp4maZP0BhUEpD5vPx0GkzoQ8oY3xOiah"
acces_token2 ="1225473463219081216-wqFZrMyFJSo0Iz8TDUH8G9Yb3RPxu9"
acces_token_secret2 = "OEuUpJRDN2IuXE92JDdfSf5O1DZBrY7Co316YoHhRTts1"
auth = tweepy.OAuthHandler(api_key2,api_key_secret2)
auth.set_access_token(acces_token2,acces_token_secret2)
API = tweepy.API(auth)
cursor = tweepy.Cursor(API.user_timeline, id ='Arbaks_Rsa',tweet_mode= "extended").items(1)
print(f"{cursor}\n")
for i in cursor:
    print(i.full_text)
    tweet_hour = i.created_at
    print(tweet_hour)
    print(i)
    format_tweet_hour = formathour(tweet_hour)
    last_tweet = i.full_text
    print(format_tweet_hour)
    last_tweet_small = last_tweet.upper()
    tweet_words = last_tweet_small.split()
    crypto_name_check()
    crypto_to_buy = crypto_name_check()
    if crypto_to_buy == "":
        print("cancel")
        break
    else:
        print(f"\n Buying {crypto_to_buy}")


    print(tweet_words)
    if  checkhour(actual_hour,format_tweet_hour) == True:
        print("7 5 0 1 4 ALPHA WANN")




