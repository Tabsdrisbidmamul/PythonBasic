# initialise a list of items in an tuple
'''
this make the list immutable (the items cannot be changed directly)
'''

print('original menu')
foods = ('beef stew', 'chicken stew',
         'chicken soup', 'beef soup',
         'water')
for food in foods:
    print(food)

'''
do this to raise an error to 
prove that it cannot be changed directly
'''
# foods.append('pork')

# rewrite the entire list to modify it
print('\nModified menu')
foods = ('pork stew', 'pork stew', 'chicken soup',
         'beef soup', 'water')
for food in foods:
    print(food)
