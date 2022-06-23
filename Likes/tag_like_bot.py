from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''
#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# Like posts based on hashtags and like 3 posts of its poster
session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
session.like_by_tags(['natgeo', 'world'], amount=10, interact=True)