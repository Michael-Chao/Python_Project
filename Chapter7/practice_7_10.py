dream_places = {}
places_active = True
while places_active:
    name = input("\nPlease enter your name: ")
    place = input("What's your dream place? ")
    dream_places[name] = place
    repeat = input("Would you like another person respond?(yes/no)")
    if repeat == 'no':
        places_active = False
print("\n---Dream Places---")
for name, place in dream_places.items():
    print(name.title() + " want to go to " + place.title() + ".")