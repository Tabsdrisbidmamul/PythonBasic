class Restaurant:
    """a simple to stimulate a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """will define what the restaurant is"""
        print(self.restaurant_name + ' is a 5 star restaurant.')
        print(self.restaurant_name + ' is open 6 times a day.')

    def open_restaurant(self):
        """stimulate that the restaurant is open"""
        print(self.restaurant_name + ' is open!')

# create an instance or set of instructions and store into variable restaurant


restaurant = Restaurant('Le de familie', 'french')
print(restaurant.restaurant_name.title() + ' is really good.')
print('They serve ' + restaurant.cuisine_type.title() + '.')

# call the two methods 
restaurant.describe_restaurant()
restaurant.open_restaurant()
