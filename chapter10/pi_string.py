with open('can.txt') as learning:
    lines = learning.readlines()

for line in lines:
    message = 'In Python you can '
    print(message.replace('Python', 'C') + line.rstrip() + ".")