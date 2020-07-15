# double asterisk it will create a dictionary with whatever the parameter
# name is, it will accept keyword arguments as a key-value pair


def build_profile(first, last, **user_information):
    """Make a dictionary to store all the information about that person"""
    person = {}
    person['first name'] = first
    person['last name'] = last
    for key, value in user_information.items():
        person[key] = value
    return person

# call the function
user_profile_0 = build_profile('steve', 'rogers', location='London', age='20',
                               field='maths')
user_profile_1 = build_profile('bob', 'pill', location='Paris', age='23',
                               field='english')
user_profile_2 = build_profile('phil', 'dill', location='rome', age='27',
                               field='biology')
print(user_profile_0)
print(user_profile_1)
print(user_profile_2)