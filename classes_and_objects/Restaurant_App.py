class Restaurant():
    def __init__(self, n, ct):
        self.restaurant_name = n
        self.cuisine_type = ct

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " serves wonderful " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open. Come on in!")


restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Create three different instances from the class, and call describe_restaurant() for each instance.
# objname=classname()
mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()  # to call methods

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango Thai', 'Thai food')
mango_thai.describe_restaurant()
