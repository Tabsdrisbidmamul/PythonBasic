# make a dictionary with people who like said programming language
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# make a list of people who have taken the poll
polling = ['jen', 'edward', 'bob', ]

# for loop to print out the keys
for key in favourite_languages.keys():
    print(key.title())

    # statement to see if the name (key) is in the polling list, if it is
    # then print the message, else invite them to take the poll
    if key in polling:
        print('  Hi ' + key.title() + ' I see your favourite programming '
                                      'language is ' + favourite_languages[
            key])
    else:
        print('  You should take the poll ' + key.title())
