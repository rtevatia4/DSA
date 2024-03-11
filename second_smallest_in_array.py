"""
Approach 1: Scan twice
Approach 2: Find in one iteration
"""

def second_smallest_approach1(arr):
    smallest = float("inf")
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    
    sec_smallest = float("inf")
    for i in range(len(arr)):
        if arr[i] < sec_smallest and arr[i] > smallest:
            sec_smallest = arr[i]
    
    return sec_smallest

def second_smallest_approach2(arr):
    smallest = float("inf")
    sec_smallest = float("inf")

    for i in range(len(arr)):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        elif arr[i] < sec_smallest and arr[i] != smallest:
            sec_smallest = arr[i]
    
    return sec_smallest

print(second_smallest_approach1([4,5,6,3,8,7,5,8]))
print(second_smallest_approach2([4,5,6,3,8,7,5,8]))