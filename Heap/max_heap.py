def heapify_maxHeap(arr, n, idx):
    largest = idx
    left = 2*idx + 1
    right = 2*idx + 2

    if left < n and arr[left] > arr[idx]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify_maxHeap(arr,n, largest)

def insert(arr, node):
    size = len(arr)
    if size == 0:
        arr.append(node)
    else:
        arr.append(node)
        for i in range((len(arr)//2) -1, -1, -1):
            heapify_maxHeap(arr, len(arr), i)

def delete(arr, node):
    size = len(arr)
    for i in range(size):
        if arr[i] == node:
            break
    arr[i],arr[size-1] = arr[size-1],arr[i]
    arr.remove(node)
    for i in range((len(arr)//2) -1, -1, -1):
            heapify_maxHeap(arr, len(arr), i)


tree = [1,4,2,3,5,7,9]
N = len(tree)//2 - 1
for i in range(N , -1, -1):
    heapify_maxHeap(tree, len(tree), i)

print(tree)

insert(tree, 10)
print(tree)
delete(tree,7)
print(tree)