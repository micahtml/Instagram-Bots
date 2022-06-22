from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#follow commenters
session.follow_commenters(['commenter1', 'commenter2'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)
