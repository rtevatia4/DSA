def binarySearch(arr, key):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2
    while start <= end:
        if key == arr[mid]:
            return ("Found",mid+1)
        if key > arr[mid]:
            start = mid+1
        else:
            end = mid - 1
        mid = (start+end)//2
    return ("Not Found",-1)

print(binarySearch([1,2,3,4,5,6,7,8,33,54,64,102], 64))