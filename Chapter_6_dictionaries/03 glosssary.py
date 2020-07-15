glossary = {
    # five python programming words and their definitions
    '.title()': 'makes the first character of all the words in the string '
                'uppercase',
    '.upper()': 'makes every letter in the string uppercase',
    '.lower()': 'makes every letter in the string lowercase',
    'sorted()': 'sorts the items into alphabetical order',
    'whitespace': 'invisible characters to represent horizontal or vertical '
                  'spaces in typography',
}

'''
for item in glossary:
    # output the key and values in dictionary
    print(item.title() + ': ' + '\n' + glossary[item].title() + '\n')
'''

# the .items() method returns key-value pairs
for key, value in glossary.items():
    print('\nWord: ' + key)
    print('Meaning: ' + value)
