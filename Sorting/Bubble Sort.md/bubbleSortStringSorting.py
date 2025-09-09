# Q) Sort a string in decreasing order of values associated after removal of values smaller than X.
# even index : string
# odd index : number
# strings and numbers are in pair

def sortTheString(str, x):

    # Create the list
    my_list = str.split()

    n = len(my_list)

    # Remove the pair whose value is less than given number x
    for i in range(n-1,0,-2):
        if int(my_list[i]) < x:
            del(my_list[i-1 : i+1])
    
    n = len(my_list)

    # sort the given list of elements
    for i in range(1, n, 2 ):
        for j in range(1, n-i, 2):
            if my_list[j] < my_list[j+2] or (my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2]):
                my_list[j], my_list[j+2] = my_list[j+2], my_list[j]
                my_list[j-1], my_list[j+1] = my_list[j+1], my_list[j-1]
    return " ".join(my_list)


str = "Akshay 43 Vishwa 79 Mohan 83 Nikhil 34 Harry 89"
print(sortTheString(str,50))