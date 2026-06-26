# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 .
# 
# Find the sum of all the primes below two million.

nums = list(range(2_000_000 + 1))
# nums = [0, 1, 2, ... 2000000]
for i in nums[2:]:
    if not i == 0:
        for n in range(i*2, 2_000_000+1, i):
            nums[n] = 0

print(sum(nums) - 1) # need to remove the 1 in the list
