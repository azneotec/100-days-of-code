class User:
    def __init__(self, user_id, username):
        # initialise attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("007", "James Bond")
user_2 = User("009", "Shane Bond")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

