#algorithims with quadratic time complexity have runtimes that grow with
#the square of the input size increases, the runtime increases quadratically

def bubble_sort(arr):
    n = len(arr)
    for  i in range(n):
        for j in range (0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Bubble sort has a time complexity of of  O(n^2). As the input list [arr] increases
#thenumber of comparissions and swaps grow quadratically.