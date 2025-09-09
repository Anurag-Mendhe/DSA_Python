# Q) Push Zeros to end while maintaining the relative order of other elements
# make use of a new array


def push_zeros_to_end(arr):
    count = 0       # count of non-zero element
    n = len(arr)
    temp = [0]*n    # temporary array

    for i in range(n):
        if(arr[i]!=0):
            temp[count] = arr[i]
            count += 1
    
    while(count < n):
        temp[count] = 0
        count += 1
    
    for i in range(n):
        arr[i] = temp[i]

arr = [1,2,0,4,3,0,5,0]
push_zeros_to_end(arr)
print(arr)
