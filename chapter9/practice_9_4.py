class Restaurant():
    """介绍一个餐馆"""
    def __init__(self, name, type):
        """餐馆的名字跟种类"""
        self.restaurant_name = name
        self.restaurant_type = type
        self.number_served = 0

    def describe_restaurant(self):
        """介绍餐馆的名字和种类"""
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The restaurant's type is " + self.restaurant_type + ".")

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print(self.restaurant_name + " is opening.")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served += number

    def increment_number_served(self, num):
        self.number_served += num

restaurant = Restaurant('sunshine', 'Chinese food')
restaurant.set_number_served(20)
restaurant.increment_number_served(20)
print("The name of the restaurant is " + restaurant.restaurant_name.title() + ".")
print("The type of the restaurant is " + restaurant.restaurant_type + ".")
print("There has " + str(restaurant.number_served) + " people have food in the restaurant.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
