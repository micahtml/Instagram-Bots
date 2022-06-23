from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''
#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#find locations by browsing: https://www.instagram.com/explore/locations/ or by searching on Instagram
session.like_by_locations(['224442573/salton-sea/'], amount=10)