# Q) How much maximum swaps are needed to sort array of length n
'''
Number of count : n*(n-1)/2
'''

def bubbleSortCountMaxSwaps(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                is_sorted = False
                count = count + 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted :
            break 
    return count
        


arr = [1,58,4,2,3,6,45,8,74]

print(bubbleSortCountMaxSwaps(arr))
