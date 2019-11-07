reponses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    reponse = input("Which mountain do you want to climb someday? ")
    reponses[name] = reponse
    repeat = input("Would you like to let another person respond？(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, reponse in reponses.items():
    print(name.title() + " would like to climb " + reponse.title() + ".")