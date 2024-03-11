
def merge(arr,l,m,r):
    left = l
    right = m+1
    k=l
    while left<=m and right<=r:
        if arr[left] <= arr[right]:
            temp[k] = arr[left]
            left+=1
        else:
            temp[k] = arr[right]
            right += 1
        k+=1

    while left<=m:
        temp[k] = arr[left]
        left+=1
        k+=1
    while right<=r:
        temp[k] = arr[right]
        right+=1
        k+=1
    # print(arr)
    # print(temp)
    for i in range(l,r+1):
        arr[i] = temp[i]
    
    return arr

def mergeSort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        arr = merge(arr,left,mid,right)
    return arr

array = [23,1,4,5,21,67,7,4,14,55,9,0,8,11,12]
temp = [0]*len(array)
print(mergeSort(array,0,len(array)-1))