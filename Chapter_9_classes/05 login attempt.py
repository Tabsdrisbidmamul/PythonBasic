class Users:
    """a simple user info data collection and greeting"""

    def __init__(self, first_name, last_name, age):
        """collect their information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0

    def describe_user(self):
        """output the user information"""
        print('\nUser information: ')
        print('\t' + self.first_name.title())
        print('\t' + self.last_name.title())
        print('\t' + str(self.age) + '\n')

    def greet_user(self):
        """personalised message to the user"""
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        print('Welcome back ' + full_name)

    def show_login_attempts(self):
        """output the login attempt"""
        print(str(self.login_attempt))

    def increment_login_attempts(self):
        """increment login attempt by 1"""
        self.login_attempt += 1

    def reset_login_attempt(self):
        """reset the login attempt back to 0"""
        self.login_attempt = 0


# create three instances to stimulate three different users
user_0 = Users(first_name='bob', last_name='phil', age=40)
user_1 = Users('phil', 'dill', 28)
user_2 = Users('anne', 'frank', 30)

# call each method for each user
user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
print()

# call the increment_login_attempts to change the attribute value
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()

# output the attribute to see if it actually incremented
user_0.show_login_attempts()

# reset the login attempt for an instance and output the result to see if it
#  actually reset
user_0.reset_login_attempt()
user_0.show_login_attempts()
