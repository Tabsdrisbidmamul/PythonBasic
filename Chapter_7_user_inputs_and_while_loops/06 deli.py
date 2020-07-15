# make a list with 3 items
sandwich_orders = ['cheese', 'chicken', 'beef', ]
# an empty list to append later items
finished_sandwiches = []

while sandwich_orders:
    # its set to true as there are items already within sandwich orders
    # store the pop() sandwiches into eaten sandwiches variable
    eaten_sandwiches = sandwich_orders.pop()

    # output a message with eaten sandwiches
    print('I made you your ' + eaten_sandwiches.title() + ' sandwich.')
    # append the eaten sandwiches into the empty list
    finished_sandwiches.append(eaten_sandwiches)

for finished_sandwich in finished_sandwiches:
    # iterate through a for loop to print out the items in finished sandwiches
    print('\nThese are the sandwiches that were made: ')
    print('\t' + finished_sandwich)
