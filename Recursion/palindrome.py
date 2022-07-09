"""
RADAR
REFER
NOON

CAR - not palindrome
"""

def isPalindrome(left,right,s):   #O(n) worst case time and space
    if (left>=right):
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(left+1,right-1,s)

s = "RADAR"
print(isPalindrome(0,len(s)-1,s))