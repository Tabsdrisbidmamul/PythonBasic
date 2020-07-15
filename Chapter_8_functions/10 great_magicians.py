# make function to print out list


def show_magicians(names):
    """iterate through the list"""
    for name in names:
        print(name)


def make_great(names):
    """add Great to the magician's name"""
    # make i as the index, by making it go to the number of items in the list
    for i in range(len(names)):
        names[i] = 'Great ' + names[i]
    print(names)


# a list of magician names
magicians = ['bob', 'phil', 'mark', ]
print(magicians)

# call the function with the magicians' names
make_great(magicians)

# call this function to show that the list has been modified
show_magicians(magicians)
