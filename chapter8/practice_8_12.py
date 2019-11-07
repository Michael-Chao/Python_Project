def need_poppings(*need):
    """顾客需要添加的食材"""
    print("\nThe customer's popping include these: ")
    for popping in need:
        print(" - " + popping)

need_poppings('fish', 'mushrooms', 'ice cream')
need_poppings('butterfly')
need_poppings('roat', 'mush', 'lise')