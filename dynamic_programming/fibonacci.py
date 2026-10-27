def recursive_fibonacci(n):
    # 0, 1, 1, 2, 3, 5, 8, 13
    if n == 0:
        return 0
    if n == 1:
        return 1

    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dp_fib(n):
    sequence = [0, 1]

    for i in range(2, n+1):
        sequence.append(sequence[i-2] + sequence[i-1])

    return sequence[n]


def fibonacci(n):
    sequence = [0, 1]
    return dp_fib(n)


n = 8
print(fibonacci(n))