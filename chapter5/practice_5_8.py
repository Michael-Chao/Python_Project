names = []
if names:
    for name in names:
        print("Welcome!" + name + ".")
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello Eric, thank you for logging again.")
else:
    print("We need to find some users!")