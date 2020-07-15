# initialize list
pizzas = ['cheese pizza', 'tomato pizza', 'chicken pizza']
# print values in list
for pizza in pizzas:
    print('I like the ' + pizza.title())

print('\nPizza is nice to eat')
# make a copy of the original list into friend_pizzas
friend_pizzas = pizzas[:]
# add a new pizza to the end of the list
pizzas.append('beef pizza')
friend_pizzas.append('pineapple pizza')

# loop over the two lists to prove they are different
print('\nmy favourite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('\nmy friend\'s favourite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)
