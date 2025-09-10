def selectionSort(arr):
    # check the size of array
    n = len(arr)

    for i in range(n):
        # consider the 0th index as the min_index
        min_index = i

        for j in range(i+1, n):
            # if any other small value is found update the min_index
            if (arr[j] < arr[min_index]):
                min_index = j
        
        # swap the values of min index and the ith element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [23,4,56,12,3,65,9]

sorted_aray = selectionSort(arr)
print("Sorted array is : ",sorted_aray)

