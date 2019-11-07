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

class IceCreamStand(Restaurant):
    """一次模拟冰淇淋店的简单尝试"""
    def __init__(self, name, type):
        """初始化冰淇淋的属性"""
        super().__init__(name, type)
        self.flavors = []

restaurant = IceCreamStand('sunshine', 'Chinese food')
restaurant.flavors = ['vanilla', 'sugar', 'chocolate']
print("The name of the restaurant is " + restaurant.restaurant_name.title() + ".")
print("The type of the restaurant is " + restaurant.restaurant_type + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("The toppings of ice cream are: ")
for flavor in restaurant.flavors:
    print(" - " + flavor.title())