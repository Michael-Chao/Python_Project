from name_function import get_formated_name
print("Please enter 'q' to quit.")
while True:
    first = input("Please enter your first name: ")
    if first == 'q':
        break
    last = input("Please enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formated_name(first, last)
    print("\tNeatly formatted name: " + formatted_name.title() + ".")