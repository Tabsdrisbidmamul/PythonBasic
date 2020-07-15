# make a dictionary with three rivers and locations
rivers = {
    'nile': 'egypt',
    'amazon rive': 'south america',
    'yangtze': 'China',
}

# .items() method returns key-value pair
for key, value in rivers.items():
    print('The ' + key.title() + ' runs through ' + value.title())

print()

# .keys() method returns only keys
for key in rivers.keys():
    print(key.title())

print()

# .values() only returns the values
for value in rivers.values():
    print(value.title())
