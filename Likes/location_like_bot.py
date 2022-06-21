from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#Pass the desired location in a string and the amount of post to send Likes
session.like_by_locations(['224442573/salton-sea/'], amount=10)