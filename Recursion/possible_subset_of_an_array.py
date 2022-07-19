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

powerset(['a','b','c'])

"""
Recursion Tree for the problem:
                             0 []
                 1 [a]                        1[]
        2[ab]           2[a]           2[b]         2[]
    3[abc]   3[ab]   3[ac]  3[a]    3[bc]  3[b]  3[c]  3[]
""" 