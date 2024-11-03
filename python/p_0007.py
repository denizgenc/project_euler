#!/usr/bin/env python3

import p_0003

def problem_0007(prime_count: int = 10001):
    primes = [2, 3, 5]
    n = 6
    while len(primes) < prime_count:
        candidate_1 = p_0003.prime_factors(n+1, start = 5)
        if len(candidate_1) == 0:
            primes.append(n+1)
        candidate_2 = p_0003.prime_factors(n+5, start = 5)
        if len(candidate_2) == 0:
            primes.append(n+5)
        n += 6
    return primes

if __name__ == "__main__":
    primes = problem_0007()
    print(f"Last 10 primes generated:\n\t{'\n\t'.join((str(x) for x in primes[-10:]))}")
    print(f"Prime 10001 is {primes[10000]}")
