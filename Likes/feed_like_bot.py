from instapy import InstaPy

#login credentials
insta_username = ''
insta_password = ''
#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# amount=100  specifies how many total likes you want to perform
# randomize=True randomly skips posts to be liked on your feed
# unfollow=True unfollows the author of a post which was considered inappropriate 
# interact=True visits the author's profile page of a certain post and likes a given number of his pictures, then returns to feed
session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)