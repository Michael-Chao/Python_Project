current_users = ['mike', 'michael', 'lily', 'tom', 'lise']
new_users = ['tom', 'charles', 'MIKE', 'jerry', 'mike']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ", you need to change a name!")
    else:
        print(new_user + ", this name has not been used!")