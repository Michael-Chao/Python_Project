prompt = "\nEnter your age, and I will tell you what's your ticket."
prompt += "\nEnter 'quit' when you finished."
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")