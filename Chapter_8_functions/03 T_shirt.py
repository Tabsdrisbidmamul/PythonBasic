# make a function that will accept two parameters
def make_shirt(size, text):
    """function to print a meesage on a t shirt and the size they want it in"""
    print('You wanted the t-shirt to be in size: ' + size)
    print('The message you wanted on the t-shirt: ' + text)

# pass the arguments in positional form
make_shirt('M', 'Python is alright')
print()
# pass the arguments in keyword form
make_shirt(size='XL', text='Java is alright')
