def get_formatted_name(first_name, last_name):
    """返回简洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name
while True:
    print("\nPlease tell me your full name: ")
    print("(enter 'q' when you want to quit)")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    full_name = get_formatted_name(first_name, last_name)
    print(full_name)