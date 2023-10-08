
def partition_on_pivot(arr,l,r):
    pivot = arr[r]
    j=l
    for i in range(l,r):
        if arr[i] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    arr[r],arr[j] = arr[j],arr[r]
    return j

def quickSort(arr, left, right):
    if left >= right:
        return
    pivot_indx = partition_on_pivot(arr,left,right)
    quickSort(arr,left,pivot_indx-1)
    quickSort(arr,pivot_indx+1,right)
    return arr

array = [6, 5, 12, 10, 9, 1, 10, 15, 8, 7, 5,0]

print(quickSort(array, 0, len(array)-1))