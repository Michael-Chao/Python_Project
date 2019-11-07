number = input("Enter a number, and I can tell you if it can be divided by ten. ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " can be divided by ten.")
else:
    print("\nThe number " + str(number) + " can not be divided by ten.")