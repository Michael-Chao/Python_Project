sandwich_orders = ['simple sandwich', 'Meat pine sandwich', 'Chicken, potato, ham, salad sandwich.']
finished_orders = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order + ".")
    finished_orders.append(current_order)
print("\n---Sandwich Menu---")
for finished_order in finished_orders:
    print(finished_order)