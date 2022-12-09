# O(2^n ) TIME COMPLEXITY
def fibonacci(n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(2))


   