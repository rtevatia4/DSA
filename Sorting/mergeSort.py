
# In place sort *kinda
# Splitting array into two halves and perform sort on both halves and then merge

def merge(arr, l, m, r):
    i=l # First half initial index
    k = l
    j=m+1   # second half inital index

    while i <= m and j <= r:
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            j+=1
        else:
            temp[k] = arr[i]
            i+=1
        k+=1
    if i>m:
        while j<=r:
            temp[k] = arr[j]
            k+=1
            j+=1
    if j>r:
        while i<=m:
            temp[k] = arr[i]
            k+=1
            i+=1
    
    for i in range(l,r+1):
        arr[i] = temp[i]


def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left+right)//2
    mergeSort(arr,left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)
    return arr



array = [6, 5, 12, 10, 9, 1, 10, 15, 8, 7, 5]
temp = [0] * len(array)
print(mergeSort(array, 0, len(array)-1))