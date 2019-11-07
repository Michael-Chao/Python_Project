names = ['admin', 'lucy', 'mike', 'art', 'lice']

for name in names:
    print("Welcome!" + name + ".")
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello Eric, thank you for logging again.")