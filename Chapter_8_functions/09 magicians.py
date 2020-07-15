# make function to print out list


def show_magicians(names):
    """Print out the name from the list"""
    for name in names:
        # iterate through the list
        print('Name: ' + name.title())

# a list of magician names


magicians = ['bob', 'phil', 'mark', ]

# call the function with the magicians' names
show_magicians(magicians)


