# set an empty dictionary to be filled up with polling later
responses = {}

# make a flag set to true
polling_active = True

while polling_active:
    # prompt for user's name and their destination
    name = input('\nWhat is your name: ')
    dream_vacation = input('What place is your dream vacation? ')

    # store the user input as key-value pair in the empty dictionary
    responses[name] = dream_vacation

    # To see if anyone wants to take the poll
    loop = input('\nWould you like another person to take this poll? ('
                 'yes/no) ')
    if loop.lower() in ['no', 'n']:
        polling_active = False

# print the results from your poll
print('\n\t---Poll Results---')
for name, dream_vacation in responses.items():
    print(name.title() + ' would like to go to ' + dream_vacation.title())
