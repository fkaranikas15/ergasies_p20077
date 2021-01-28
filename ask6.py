import tweepy
consumer_key= 'API key'
consumer_secret= 'API key secret'
access_token= 'Access token'
access_token_secret= 'Access token secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)




tweets=[]
user = api.get_user("put an username")
user_timeline= user.timeline()
for i in range(9):
    tweets.append(user_timeline[i].text)
    #print(tweets[i])
file=""
for i in range(9):
    if (i!=9):
        file=file+tweets[i]+" "
    else:
        file=file+tweets[i]



word = ""
all_words = []
for i in range(0, len(file)):
    if(file[i] !=" "):
        word = word + file[i]
    else:
        all_words.append(word)
        word = ""
all_words.sort(key=len)
ar_small=[]
ar_largest=[]
for i in range(5):
    ar_small.append(all_words[i])
for i in range(-1,-6,-1):
    ar_largest.append(all_words[i])
for i in range(5):
    print("H",i+1,"h mikroterh lejh einai",ar_small[i])
for i in range(5):
    print("H",i+1,"h megaluterh lejh einai",ar_largest[i])
