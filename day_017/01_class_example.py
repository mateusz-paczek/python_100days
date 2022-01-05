class User:
    # Initialize attributes
    def __init__(self, user_id, username):
        # print("New user is created")
        self.id = user_id
        self.username = username
        self.followers = 0 # Provide default value
        self.following = 0 # Provide defaul value
    def follow(self, user):
        user.followers += 1
        self.following += 1
        


user_1 = User("001","Mateusz")
user_2 = User("002", "Stas")
#user_1.id = "001"
#user_1.username = "mateusz"

# print(user_1.username)
# print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)


print(user_2.followers)
print(user_2.following)