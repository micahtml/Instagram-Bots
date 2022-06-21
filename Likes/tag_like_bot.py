from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#Pass desired tags in strings in the first argument and the Like limit in second argument
session.like_by_tags(["cars", "Ferari"], amount=10)