def fibonacci(n):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq

print(fibonacci(16))
