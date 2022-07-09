"""
Power Set: set of all possible subset of arr
{a,b,c} --> {a},{b},{c},{a,b},{a,c},{b,c},{a,b,c}
"""

def powerset_helper(arr,i,subset):
    if i ==len(arr):
        #ans.append(subset)
        print(subset)
        return
    subset.append(arr[i])
    powerset_helper(arr,i+1,subset)
    subset.pop()
    powerset_helper(arr,i+1,subset)

def powerset(arr):
    subset = []
    powerset_helper(arr,0,subset)

powerset(['a','b','c','d'])