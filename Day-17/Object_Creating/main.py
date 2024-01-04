class User:
    def __init__(self,user_id , username):
        self.id = user_id
        self.name = username
        self.followers = 0


user_1 = User("001" , "Min Zayar Maung")
user_2 = User("002" , "Zayar Min Maung")

print(user_1.followers)