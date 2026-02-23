def is_sorted(arr):
    pos_ant = 1
    if arr[0] < arr[1]:sort = "Ascending"
    else:sort = "Descending"
    for i in range(2,len(arr)):
        if arr[pos_ant] < arr[i]:new_sort = "Ascending"
        else:new_sort = "Descending"
        if new_sort != sort: return "Not sorted"


    return sort

if __name__ == '__main__':
    print(is_sorted([1, 2, 3, 4, 5]))
    print('--------')
    print(is_sorted([10, 8, 6, 4, 2]))
    print('--------')
    print(is_sorted([1, 3, 2, 4, 5]))
    print('--------')
    print(is_sorted([3.14, 2.71, 1.61, 0.57]))
    print('--------')
    print(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]))
    print('--------')
    print(is_sorted([0.4, 0.5, 0.3]))
    print('--------')