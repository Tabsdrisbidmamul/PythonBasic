# function that will use a dictionary to store information
# one of the parameters is optional


def make_album(name, title, no_of_album=''):
    """Store the arguments in the dictionary"""
    artist = {'artist': name, 'artist_title': title, }
    # python interprets non-empty strings as true
    if no_of_album:
        # store the value given into the dictionary
        artist['number of album'] = no_of_album
    return artist

# make the loop true so it will run forever


while True:
    # prompt the user to input their name and tell them how to end the program
    print('\nplease enter your name: ')
    print('press \'q\' to end the program')

    # store their name into f_name
    f_name = input('Your name: ')
    if f_name.lower() == 'q':
        break

    # store their artist title into artist_title
    artist_title = input('Your  artist title: ')
    if artist_title.lower() == 'q':
        break

    # ask them if they have any albums
    q_have_an_album = input('Do you have any albums? (yes/no) ')
    # if they do then ask them how many
    if q_have_an_album.lower() == 'yes':
        album_count = input('How many do you have? ')
        # once attained call the function and store all the information into
        # the dictionary and print it
        musician_0 = make_album(f_name, artist_title, album_count)
        print(musician_0)
    elif q_have_an_album.lower() == 'q':
        break
    else:
        # if not then store their name and title into the dictionary and
        # print it
        musician_1 = make_album(f_name, artist_title)
        print(musician_1)
