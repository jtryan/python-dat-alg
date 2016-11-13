# Bubble sort optimized avoid n-1 items
def bubblesort(arr):
    n = len(arr)
    swapped = True
    while (swapped):
        swapped = False
        for index in range(0,n-1,1):
            if arr[index] > arr[index+1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
                swapped = True
    n -= 1

    return arr

print bubblesort([21,4,1,3,9,20,25,6,21,2,14])

