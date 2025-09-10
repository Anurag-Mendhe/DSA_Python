def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        # j is initialized to the index of last element in the sorted portion of array
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


arr = [23,85,6,1,27,32]
print("Sorted array is : ",insertion_sort(arr))

