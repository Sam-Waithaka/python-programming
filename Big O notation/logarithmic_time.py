#logarthimic time complexity have runtimes that grow logarithmically with the size 
#of the input data. 
#logarthim time complexity os considered very efficient.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1 

    return -1
#The function above is a implementation of the Binary Search algorithm.
#This function receive two parameters, an array and a target value to search for in this arraya