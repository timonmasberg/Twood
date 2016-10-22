from textblob_de import TextBlobDE as TextBlob
import twitter_interface as ti

# get tweets by hashtag
tweets = ti.get_tweets("#jugendhackt", 365, 100)

negative  = 0
positive = 0
neutrale = 0

# go through tweets and get mood
for tweet in tweets:
    blob = TextBlob(tweet)
    sentiment = blob.sentiment[0]
    if sentiment > 0:
        positive += 1
    elif sentiment < 0:
        negative += 1
    else:
        neutrale += 1

# calculate mood in per cent
gesamt_anzahl_bewertbar = float(negative+positive)#+neutrale
prozent_negativ = (negative/gesamt_anzahl)*100.0
prozent_positiv = (positive/gesamt_anzahl)*100.0
#prozent_neutral = (neutrale/gesamt_anzahl)*100.0

gesamt_anzahl= negative+positive+neutrale

moodstr = ""
if prozent_negativ > prozent_positiv:
	moodstr = "Die Stimmung ist eher negativ"
elif prozent_negativ < prozent_positiv:
	moodstr = "Die Stimmung ist eher positiv"
else:
	moodstr = "Die Stimmung ist ausgeglichen"


