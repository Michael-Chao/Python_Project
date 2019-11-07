sandwich_orders = ['pastrami sandwich', 'simple sandwich', 'pastrami sandwich', 'Meat pine sandwich', 'Chicken, potato, ham, salad sandwich.', 'pastrami sandwich']
finished_orders = []
print(sandwich_orders)
print("We have no pastrami sandwich at all.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order + ".")
    finished_orders.append(current_order)
print("\n---Sandwich Menu---")
for finished_order in finished_orders:
    print(finished_order)