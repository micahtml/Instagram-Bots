from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#follow by tag
session.follow_by_tags(['hashtag1', 'hashtag2', 'hashtag3'], amount=5)