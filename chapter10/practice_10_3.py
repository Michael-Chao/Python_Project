filename = 'reason.txt'

reason =
while True:
    name = input("Please enter your name:")
    print("Welcome, " + name.title() + ".")
    with open(filename, 'w') as project_name:
        project_name.write(name)