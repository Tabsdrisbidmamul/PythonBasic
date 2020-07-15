# make prompt to input into the input() method
prompt = '\nEnter your age please:'
prompt += '\n(enter \'200\' when you\'re done). '

while True:
    # set while to true so it runs forever
    # make the age variable store the user input and make it into a int
    age = abs(int(input(prompt)))

    # have price initial set at 0
    price = 0
    # test the user's input and give it a price
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif (age >= 12) and (age < 110):
        price = 15
    elif age == 200:
        print('\nSee you soon')
        # exit loop if user does enter 200
        break
    else:
        print('\nplease input a correct age please')

    # output the price at the end to the user
    print('\nThe price for your admission is $' + str(price))
