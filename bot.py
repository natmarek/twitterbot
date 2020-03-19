import tweepy

auth = tweepy.OAuthHandler('PsoryXV0EemONu6lqVoRPkZqj', '28HyWsExTeYHAhazOL2nN69XTdC9gL1p9sMTInMlki48w3JQJV')
auth.set_access_token('1240768744810582018-R7J1pMA7dKjLSmKjksKL3NgbRmQKsk', 'fOh7mjcFrEO65bIBwJ2eHuiI6W5Uyg440MyiH22pupxWs')

api = tweepy.API(auth)
user = api.me()
print(user.screen_name)
    