class Restaurant:
    """a simple to stimulate a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """will define what the restaurant is"""
        print(self.restaurant_name + ' is a 5 star restaurant.')
        print(self.restaurant_name + ' is open 6 times a day.')

    def open_restaurant(self):
        """stimulate that the restaurant is open"""
        print(self.restaurant_name + ' is open!')

    def show_number_served(self):
        """output the the number served attribute"""
        print('This restaurant has served ' + str(self.number_served))

    def set_number_served(self, number_served):
        """update the number served through function call by passing it as
        an argument"""
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print('you cannot go backwards in time')

    def increment_number_served(self, increase_number_served):
        """increment the number served depending on the argument passed"""
        self.number_served += abs(increase_number_served)


# create an instance or set of instructions and store into variable restaurant
restaurant = Restaurant('Le de familie', 'french')
print(restaurant.restaurant_name.title() + ' is really good.')
print('They serve ' + restaurant.cuisine_type.title() + '.')

# call the two methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
# set the number served attribute manually
restaurant.number_served = 5
restaurant.show_number_served()

restaurant.number_served = 10
restaurant.show_number_served()
print()

# pass an argument through the function call to update the an attribute
# through method
restaurant.set_number_served(20)
restaurant.show_number_served()
print()

# pass an argument to function call to update attribute by incrementing it
restaurant.increment_number_served(50)
restaurant.show_number_served()
