#x^n

def pow(x,n):     #O(n) solution (Time and space)
    if n==0:
        return 1
    partialAns = pow(x,n-1)
    return x*partialAns

def pow_optimized(x,n):     #O(log n) solution
    if n==0:
        return 1
    temp = pow(x,n//2)
    if n%2==1:
        return temp*temp*x
    return temp*temp

print(pow(4,3))
print(pow_optimized(4,3))