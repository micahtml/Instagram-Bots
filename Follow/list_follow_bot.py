from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#follow by list
session.follow_by_list(['hardy', 'keenu'], times=1, sleep_delay=600, interact=False)