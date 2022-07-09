

def reverse(left, right, arr):
    if left>=right:
        return 
    arr[left], arr[right] = arr[right], arr[left]
    reverse(left+1, right-1, arr)
    #return arr

arr = [1,2,3,4,5]

print(reverse(0,len(arr)-1,arr))
print(arr)