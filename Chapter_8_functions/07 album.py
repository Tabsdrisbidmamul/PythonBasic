# function that will use a dictionary to store information
# one of the parameters is optional


def make_album(name, title, no_of_album=''):
    artist = {'artist': name, 'artist_title': title, }
    # python interprets non-empty strings as true
    if no_of_album:
        # store the value given into the dictionary
        artist['number of album'] = no_of_album
    return artist

# call the function and print the result


musician_0 = make_album('steve', 'rogers', no_of_album=str(3))
print(musician_0)
musician_1 = make_album('bob', 'micheal')
print(musician_1)
musician_2 = make_album('phil', 'bill')
print(musician_2)
