# make a function that has 2 default parameters
def make_shirt(size='L', text='I love Python'):
    """function to print a meesage on a t shirt and the size they want it in"""
    print('You wanted the t-shirt to be in size: ' + size)
    print('The message you wanted on the t-shirt: ' + text)

# pass only one argument, and use the other one as a default value
make_shirt(size='M')
print()
# change both the default values and pass your own arguments
make_shirt(size='S', text='I like Pascal')