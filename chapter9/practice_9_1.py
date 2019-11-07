class Restaurant():
    """介绍一个餐馆"""
    def __init__(self, name, type):
        """餐馆的名字跟种类"""
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        """介绍餐馆的名字和种类"""
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The restaurant's type is " + self.restaurant_type + ".")

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print(self.restaurant_name + " is opening.")

restaurant = Restaurant('sunshine', 'Chinese food')
print("The name of the restaurant is " + restaurant.restaurant_name.title() + ".")
print("The type of the restaurant is " + restaurant.restaurant_type + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('hot pot', 'Chinese food')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Apolo', 'Fashion')
restaurant_3.describe_restaurant()