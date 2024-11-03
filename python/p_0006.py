#!/usr/bin/env python3

def tri(n: int) -> int:
    return (n * (n + 1)) // 2

# derived this out on pen and paper lmao
def pyr(n: int) -> int:
    return (n * (n + 1) * ((2*n) + 1)) // 6

def problem_0006():
    return (tri(100) ** 2) -  pyr(100)

if __name__ == "__main__":
    print(problem_0006())
