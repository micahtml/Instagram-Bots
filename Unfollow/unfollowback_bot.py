from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#Unfollow the back followers
session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=600)
