#!/usr/bin/env python3

def prime_factors(n: int) -> set[int]:
    pfactors = set()
    for f in range(2, int(n ** 0.5) + 1):
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
