usernames = []

'''
if a empty list is tested in the if statement, an empty list will return 
false so the if statement will run the 'else' part of the code. if there is 
at least one item in the list, then it will return true when tested and will 
run the 'if' part of the code
'''
if usernames:   # will return false when tested
    for username in usernames:  # run a for loop going though names
        if username == 'admin':  # check to see if admin is list
            print('Hello Admin, would you like to see the status report?')
        else:  # print regular message for everything else
            print(
                'Hello %s, thank you for logging in today' % username.title())
else:
    print('Need to find some users!')