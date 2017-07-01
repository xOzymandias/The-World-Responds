#import modules
import tweepy, time, sys

#Change notes
#
#Clean up code, improve comments
#Retweet any replies, check on each cycle.
#Search for a new tweet each time instead of grabbing a list of tweets and cycling through
#

#global variables
VERSION_NUMBER = "1.1beta"
CONSUMER_KEY = '5fUoGfswHm6NHUImDLlYmZLL2'
CONSUMER_SECRET = 'YQqmp8MbupaCt7t147vBaXYulFBKMm0qn1gSruootyKYmkXznx'
ACCESS_KEY = '872552290913329155-eL2AeyHUm25fpgqpRxv1QETEoLF93eG'
ACCESS_SECRET = 'TNA1o9p3gpIZLc9lcWjXJrnVoYxogVNCfGRqY8OdBpar0'

#Main
print ('-----------------')
print ('The World Responds Bot')
print ('Christopher Kitzmiller')
print ('Version Number: ', VERSION_NUMBER)
print ('Connecting to Twitter...')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


while True:
	#respond to tweets containing "hello world"
	for tweet in tweepy.Cursor(api.search, q='"hello world"').items(1):
		try:
			if hasattr(tweet, 'retweeted_status') == False:
                                #Variables
				id = tweet.id
                                #Console print
				print('-----------------')
				print(id)
				print(tweet.text)
                                response = "@%s hi" % (tweet.user.screen_name)
				print('@' + tweet.user.screen_name + ' hi')
                                #Reply to status on Twitter
				api.update_status(response, tweet.id)
				#Wait, so Twitter doesn't blacklist you
				time.sleep(900)
		except tweepy.error.TweepError:
			print("Error responding to tweet")
	#Check for and retweet any replies
        #Skip any Tweets that were already retweeted
	for reply in tweepy.Cursor(api.search, q='@World_Responds').items(1):
		try:
			api.retweet(reply.id)
			time.sleep(900)
			break
		except tweepy.error.TweepError:
			print("Error while retweeting")
			break
