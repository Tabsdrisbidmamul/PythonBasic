class Restaurant:
    """a simple to stimulate a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """will define what the restaurant is"""
        print(self.restaurant_name.title() + ' is a 5 star restaurant.')
        print(self.restaurant_name.title() + ' is open 6 times a day.\n')

    def open_restaurant(self):
        """stimulate that the restaurant is open"""
        print(self.restaurant_name.title() + ' is open!')

# create an instance or set of instructions and store into variable restaurant
# create three different instance


restaurant = Restaurant('Le de familie', 'french')
restaurant_1 = Restaurant('taste of hong kong', 'chinese')
restaurant_2 = Restaurant('Days', 'buffet')

print(restaurant.restaurant_name.title() + ' is really good.')
print('They serve ' + restaurant.cuisine_type.title() + '.')
print()
# call the two methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
# call the three instances, call call method describe_restaurant() for each one
restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
