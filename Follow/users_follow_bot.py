from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#follow by followers
session.follow_user_followers(['follower1', 'follower2'], amount=10, randomize=False, interact=True)
