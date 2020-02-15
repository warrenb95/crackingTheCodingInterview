# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr, low, high, pivot): 
    while low <= high:
        while arr[low] < pivot:
            low += 1
        
        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    return low

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        
        pivot = arr[(low + high ) // 2]

        index = partition(arr, low, high, pivot)
  
        quickSort(arr, low, index - 1) 
        quickSort(arr, index, high)

arr = [9,34,35,6,63,3,5,6,7,78,1]
n = len(arr)

quickSort(arr, 0, n - 1)

print(arr)