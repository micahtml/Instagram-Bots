
from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)