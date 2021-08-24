"""
given n return the nth number in the fibonacci sequence
"""

memo = {}

def fib(n):

    if n in memo:
        return memo[n]

    elif n <=2:
        memo[n] = 1
        return 1       
    else:
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]

print(fib(5))
print(fib(7))
print(fib(10))
print(fib(50))