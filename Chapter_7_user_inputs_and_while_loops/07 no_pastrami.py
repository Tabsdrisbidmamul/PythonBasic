# output a message to say we've ran out of pastrami
print('We\'ve ran out of pastrami sandwiches')

# list with at least pastrami within it 3 times
sandwich_orders = ['cheese', 'pastrami', 'chicken', 'pastrami', 'beef',
                   'pastrami', ]
# empty list to append the pop sandwiches later
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    # makes sure that pastrami is removed from the list
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    # second while loop to pop() and append() the sandwiches that are not
    # pastrami into the empty list
    eaten_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(eaten_sandwiches)

for finished_sandwich in finished_sandwiches:
    # iterate through the filled list now
    print('\nThese are the sandwiches that were made')
    print('\t' + finished_sandwich.title())
