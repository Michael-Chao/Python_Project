favorite_numbers = {
    'liu': [1, 9, 18],
    'hao': [3, 9, 12, 87],
    'xu': [8, 6, 9, 0, 1000],
    'li': [2, 4, 7, 8, 32],
    'lu': [7, 67, 2098, 35353663],
    }
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
