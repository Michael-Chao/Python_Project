def describe_pet(animal_type = 'dog', animal_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + animal_name.title() + ".")
describe_pet(animal_name= 'harry')