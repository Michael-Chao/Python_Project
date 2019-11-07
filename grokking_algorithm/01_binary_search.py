def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        num = list[mid]
        if num > item:
            low = low + 1
        elif num < item:
            high = high - 1
        else:
            return mid

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5))
print(binary_search(my_list, 1))