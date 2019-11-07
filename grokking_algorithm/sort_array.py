def findsmallest(arr):
    """找到数组中最小值"""
    small_num = arr[0]
    small_num_sub = 0
    for num in range(1,len(arr)):
        if arr[num] < small_num:
            small_num = arr[num]
            small_num_sub = num
    return small_num_sub

def selectionsort(arr):
    new_arr = []
    for i in range(len(arr)):
        arr_num = findsmallest(arr)
        new_arr.append(arr.pop(arr_num))
    return new_arr

print((selectionsort([5, 6, 2, 10, 3])))