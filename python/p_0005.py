#!/usr/bin/env python3
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
# remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# numbers 1 to 10:
# prime factors: 2, 3, 5, 7
# has 8 and 9: 2^3, 3^2
# 2^3 * 3^2 * 5 * 7 = 2520

# So I guess you're just supposed to get a list of the prime factors and their heighest power, then
# find the product of all of those

import math

import p_0003

def get_factor_powers(n: int) -> dict[int: int]:
    factor_powers = dict()
    prime_factors = p_0003.prime_factors(n)

    if len(prime_factors) == 0: # n is a prime number
        return {n: 1}
    for f in prime_factors:
        power = 1
        dividend = n / f
        while dividend % f == 0:
            power += 1
            dividend /= f
        factor_powers[f] = power

    return factor_powers

def lcm(nums: list[int]) -> int: # If I was cool this would take a generic iterable of ints instead
    factor_powers = {}
    for n in nums:
        n_factor_powers = get_factor_powers(n)
        for k, v in n_factor_powers.items():
            if k in factor_powers:
                if v > factor_powers[k]:
                    factor_powers[k] = v
                continue
            factor_powers[k] = v
    return math.prod([k ** v for k, v in factor_powers.items()])

def problem_0005():
    return lcm(list(range(1, 21)))

if __name__ == "__main__":
    print(problem_0005())
