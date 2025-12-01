def sortR(arr):
    n = len(arr)

    if n <= 4:
        return insertionSort(arr)
    
    first_arr_a = sortR(arr[:n*3//4])
    merged_arr_b_a = sortR(first_arr_a[n//4:] + arr[n*3//4:])
    merged_arr_b_c = sortR(first_arr_a[:n//4] + merged_arr_b_a[:n//2])
    return merged_arr_b_c + merged_arr_b_a[n//2:]

 
def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while  j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


print(sortR([12, 11, 13, 5, 6, 23, 46, 2, 8, 78]))