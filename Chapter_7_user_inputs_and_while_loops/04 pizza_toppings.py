# make a prompt to act as the message
prompt = '\nEnter the type of topping you want on your pizza:'
prompt += '\n(enter \'quit\' to exit the program). '

# make the loop set to true for it to run forever
while True:
    # store the input into a variable called topping
    topping = input(prompt)

    if topping.lower() == 'quit':
        # exit out of the loop when the user inputs quit
        break
    else:
        # print the out a message to the user
        print('You\'ll adding this to the topping: ' + topping.title())
