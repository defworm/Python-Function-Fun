#Uses recursion to find the factorial of an integer.

def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(3))
print(recursive_factorial(6))