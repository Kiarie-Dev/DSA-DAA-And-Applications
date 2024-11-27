# Insertion sort 
def insertionSort(Arr):
    n = len(Arr)
    for i in range(1, n):
        temporaryVar = Arr[i]
        # insert A[i] into the sorted subarray
        j = i - 1
        while j >= 0 and Arr[j] > temporaryVar:
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j + 1] = temporaryVar

# Example usage
Arr = [5, 2, 4, 6, 1, 3]
insertionSort(Arr, n)
print("Sorted array is: ", Arr)
