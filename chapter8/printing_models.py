unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
printed_designs = []
while unprinted_design:
    current_design = unprinted_design.pop()
    print("Printing model: " + current_design)
    printed_designs.append(current_design)

print("\nThe following models have been printed: ")
for printed_design in printed_designs:
    print(printed_design)