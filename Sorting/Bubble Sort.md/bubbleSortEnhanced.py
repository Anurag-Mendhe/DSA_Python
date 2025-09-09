def bubbleSortEnhanced(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(j-i-1):
            is_sorted = False
            if(arr[j]  > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted:
            break        

arr = [1,2,3,4,5]

bubbleSortEnhanced(arr)
print(arr)

