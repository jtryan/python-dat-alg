"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quicksort(array, lo, p - 1)
        quicksort(array, p + 1, hi)

    return array


# def partition(array, lo, hi):
#     pivot = array[hi]
#     i = lo # swap area
#     for j in range(lo, hi - 1):
#         if array[j] <= pivot:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#     array[i], array[hi] = array[hi], array[i]
#     return i

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, len(test)-1)



