"""
Certain positive integers have their decimal representation consisting only of ones and zeros, 
and having at least one digit one, e.g. 101. If a positive integer does not have such a property, 
one can try to multiply it by some positive integer to find out whether the product has this property.

Input
Number K of test cases (K is approximately 1000);
in each of the next K lines there is one integer n (1 <= n <= 20000)
Output
For each test case, your program should compute the smallest multiple of the number n consisting only 
of digits 1 and 0 (beginning with 1).

Example
Input:
3
17
11011
17
Output:
11101
11011
11101
"""



import collections


def one_zero(n):
    queue = collections.deque([1])
    while queue:
        node = queue.popleft()
        if node%n == 0:
            return node
        else:
            queue.append(node*10)
            queue.append(node*10+1)
            
cases = int(input())
for test in range(cases):
    print(one_zero(int(input())))