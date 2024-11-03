#!/usr/bin/env python3
# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# the product of two 3 digit numbers will be 5 or 6 digits long.
# A 6 digit palindrome will have the digits abccba, where a != 0.
# This will be equal to ax^5 + bx^4 + cx^3 + cx^2 + bx + a
# or a(x^5 + x^0) + b(x^4 + x^1) + c(x^3 + x^2), where x = 10 for decimal numbers

# Two three digit numbers can be expressed as (dx^2 + ex + f) and (gx^2 + hx + i)
# so their product would be dgx^4 + dhx^3 + dix^2 + egx^3 + ehx^2 + eix + fgx^2 + fhx + fi
# = dgx^4 + (dh + eg)x^3 + (di + eh + fg)x^2 + (ei + fh)x + fi

# since the palindrome means the first and last digit are the same, we know that the first digit
# a = fi mod 10
# The first digit ax^5 somehow also has to be set by dgx^4 + (dh_eg)x^3 + ...
# That means we're looking for a 2 digit number for dg (it doesn't have to be, given that if it is a
# single digit number, the contribution from (dh + eg)x^3 can carry to dgx^4, but it's unlikely and
# we're trying to find the _biggest_ palindrome anyway...)
# therefore floor(dg / 10) = fi mod 10 --OR-- floor(dg / 10) + n = fi mod 10
#   the + n option on the right is due to carrying from lower digits

# If we want to find a palindrome which is of the form 9xxxx9, we know we can't reach that with just
# dg because the largest number possible by multiplying two single digit numbers is 81. So we need a
# contribution from the middle digits.
# Also it means that fi is either (1, 9) or (3, 3)...

# I give up, I think I'm just going to iterate and check.


def get_factor_pairs(n: int, start: int = 2) -> tuple[int, int]:
    """
    start is for what number to start from for finding factors, purely for problem 4's 3 digit
    number requirement
    """
    for i in range(start, int(n ** 0.5) + 1):
        if n % i == 0:
            yield (i, n//i)

def all_factor_pairs(n: int, start: int) -> list[tuple[int, int]]:
    return list(get_factor_pairs(n, start))


def problem_0004():
    num = 999_999
    for _a in range(9):
        for _b in range(9):
            for _c in range(9):
                for pair in get_factor_pairs(num, start=100):
                    if pair[1] < 999:
                        return pair
                # couldn't find three digit factor pair, go to next --cc-- iteration
                num -= 1100
            # couldn't find three digit factor pairs for any of the --cc-- iterations for the
            # current value of b, go to next -b--b- iteration
            # since we've subtracted 9900 already, and subtracting 1 from -b--b- is = -10010, we
            # only need to subtract 10010 - 9900 = 110
            num -= 110
        else:
            # we need to check the centre one more time. right now we're at - 90090, we need to be
            # at -99990
            for _c in range(9):
                for pair in get_factor_pairs(num, start=100):
                    if pair[1] < 999:
                        return pair
                num -= 1100
        # couldn't find three digit factor pairs for any of the -bccb- iterations for the current
        # value of a, go to next a----a iteration
        # since we've subtracted 99990 already, all we need to subtract is 100001 - 99990 = 11
        num -= 11
    return "lmao"

if __name__ == "__main__":
    pair = problem_0004()
    print(f"palindrome {pair[0] * pair[1]} is made up of factors {pair}")
