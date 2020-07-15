current_users = ['sarah', 'alice', 'phil',
                 'john', 'bob']   # a list of five names

new_users = ['JOHN', 'alice', 'william',
             'james', 'ruby']   # list of 3 unique names 2 are already in
# the first list

for user in new_users:   # loop through second list, its case insensitive
    if user.lower() not in current_users:   # if the second list names do
        # not appear in the first list, then execute the print
        print('The username %s is available' % user.title())
    else:   # if the second list names do appear in the first list,
        # then execute the print
        print('Username %s is already taken, please choose a different '
              'username' % user.title())
