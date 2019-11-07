class User():
    """存储用户的信息"""

    def __init__(self, first, last, age, gender):
        """用户的信息"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        self.full_name = self.first_name + ' ' + self.last_name
        print("Here are the user's information: " + self.full_name + ", " + str(self.age) + ", " + self.gender + ".")

    def greet_user(self):
        """向用户打招呼"""
        print("Welcome, " + self.full_name + "!")

    def increment_login_attempts(self):
        """将属性login_attempts的值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts 重置为0"""
        self.login_attempts = 0

user = User('Chao', 'Xu', 24, 'man')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
