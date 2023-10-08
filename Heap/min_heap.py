def heapify_minHeap(arr, n, idx):
    smallest = idx
    left = 2*idx + 1
    right = 2*idx + 2

    if left < n and arr[left] < arr[idx]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right 
    
    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[i]
        heapify_minHeap(arr,n, smallest)

tree = [1,4,2,3,5,7,9]
for i in range(len(tree)//2 -1 , -1, -1):
    heapify_minHeap(tree, len(tree), i)

print(tree)