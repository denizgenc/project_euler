#!/usr/bin/env python3

def prime_factors(n: int, start: int = 2) -> set[int]:
    """
    return a set of the prime factors of n, not including n itself.
    Therefore if n is prime, returns empty set.

    start is for which number to start doing prime tests from
    Set to 5 if you've already sieved out {0, 2, 3, 4} mod 6
    """
    pfactors = set()
    for f in range(start, int(n ** 0.5) + 1):
        if n % f == 0:
            pfactors.add(f)
            complement = n // f
            complement_factors = prime_factors(complement) # recursive calls ...
            if len(complement_factors) == 0: # complement to this prime factor was prime itself
                pfactors.add(complement)
            else:
                pfactors.update(complement_factors)
            break # recursive calls found all our prime factors, don't need to keep looping
    return pfactors

def problem_0003():
    return prime_factors(600851475143)

if __name__ == "__main__":
    print(problem_0003())
