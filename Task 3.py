def fibonacci(n):
    """Return the first n numbers in the Fibonacci series."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = 10 
fib_sequence = fibonacci(n)
print(fib_sequence)
