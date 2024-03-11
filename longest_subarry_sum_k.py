"""
Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.

"""
# Brute force O(n^2)
# def getLongestSubarrayLength(arr,k):
#     longest = 0
#     for i in range(len(arr)):
#         curr_sum = 0
#         for j in range(i,len(arr)):
#             curr_sum += arr[j]
#             if curr_sum == k:
#                 longest = max(longest,j-i+1)
        
#     return longest

def getLongestSubarrayLength(arr,k):
    longest = 0
    right = 0
    left = 0
    curr_sum = 0
    while right < len(arr):
        curr_sum += arr[right]
        # print(left,right,curr_sum)
        if curr_sum == k:
            longest = max(longest, right-left+1)
        while left <= right and curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        
        right+=1
    return longest

if __name__ == "__main__":
    a = [2,3,5,0,0,0,0,9,1,9]
    k = 10
    print(getLongestSubarrayLength(a,k))
