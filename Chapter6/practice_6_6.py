favorite_lanuages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
people = ['jen', 'edward']
for name in favorite_lanuages.keys():
    if name in people:
        print("Thank you, " + name.title() + "!")
    else:
        print("Welcome you to join us, " + name.title() + "!")