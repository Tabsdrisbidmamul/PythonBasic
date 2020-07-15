# make function to print out list


def show_magicians(names):
    """iterate through the list"""
    for name in names:
        print(name.title())


def make_great(names):
    """add Great to the magician's name"""
    # make i as the index, by making it go to the number of items in the list
    for i in range(len(names)):
        names[i] = 'Great ' + names[i].title()
    return names


# a list of magician names
magicians = ['bob', 'phil', 'mark', ]


# call the function with the magicians' names
copy = make_great(magicians[:])
print(copy)
# call the function to show that list has not been modified
show_magicians(magicians)
