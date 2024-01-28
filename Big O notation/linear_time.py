# Linear time example

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
        return False
    
#As the size of the list (arr) increases, the number of iterations the 
#loop performs also increases linearly. 
#Therefore, this algorithm has a time complexity of O(n).
    