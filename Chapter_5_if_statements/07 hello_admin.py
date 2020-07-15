usernames = [
    'admin', 'john', 'alice',
    'sarah', 'phil']    # initialize a list of name

for username in usernames:   # run a for loop going though names
    if username == 'admin':   # check to see if admin is list
        print('Hello Admin, would you like to see the status report?')
    else:   # print regular message for everything else
        print('Hello %s, thank you for logging in today' % username.title())

