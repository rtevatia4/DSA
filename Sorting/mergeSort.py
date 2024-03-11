
# In place sort *kinda
# Splitting array into two halves and perform sort on both halves and then merge
def merge(a,l,m,r):
    i=l
    k=l
    j=m+1
    while i<=m and j<=r:
        if a[i] > a[j]:
            temp[k] = a[j]
            j+=1
        else:
            temp[k] = a[i]
            i+=1
        k+=1
    
    while i<=m:
        temp[k] = a[i]
        k+=1
        i+=1
    while j<=r:
        temp[k] = a[j]
        k+=1
        j+=1
    
    for i in range(l,r+1):
        a[i] = temp[i]
    
    return a

def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left+right)//2
    mergeSort(arr, left,mid)
    mergeSort(arr, mid+1, right)
    arr = merge(arr,left,mid,right)
    return arr


array = [6, 5, 12, 10, 9, 1, 10, 15, 8, 7, 5,-1]
temp = [0] * len(array)
print(mergeSort(array, 0, len(array)-1))