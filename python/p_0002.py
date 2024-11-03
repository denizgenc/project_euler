#!/usr/bin/env python3

def fib(a = 1, b = 1, n = 0):
    """
    n is number of iterations, non-positive n is infinite
    """
    if n > 0:
        for _ in range(n):
            yield b
            b, a = b+a, b
    else:
        while True:
            yield b
            b, a = b+a, b


def problem_0002():
    evens = []
    for i in fib():
        if i >= 4_000_000:
            break
        if i % 2 == 0:
            evens.append(i)
    return sum(evens)

if __name__ == "__main__":
    print(problem_0002())
