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

# make a class that inherent Restaurant class by passing it as an argument


class IceCreamStand(Restaurant):
    """stimulate an ice-cream stand"""

    # the __init__ will have the same parameters as the parent class
    def __init__(self, restaurant_name, cuisine_type):
        # the super() function provides a connection between the parent and
        # child class
        super().__init__(restaurant_name, cuisine_type)
        # the child class will inherent everything from the parent class,
        # the child class can have its own attributes/methods that are
        # exclusive only to the child class
        self.flavours = ['chocolate', 'strawberry', 'vanilla', 'mint', ]

    def display_ice_cream_flavours(self):
        print('These are the flavours: ' + str(self.flavours))

    def describe_restaurant(self):
        """will define it is ice cream stall"""
        print(self.restaurant_name + ' is a good ice cream stall.')
        print(self.restaurant_name + ' is open 4 times a day.')


# function call
customer_0 = IceCreamStand('Ice-Cream Stand', 'deserts')
customer_0.display_ice_cream_flavours()
customer_0.describe_restaurant()
