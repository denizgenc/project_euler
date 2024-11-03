#!/usr/bin/env python3

def problem_0001():
    return sum([a for a in range(1000) if not ((a % 3) and (a % 5)) ])

if __name__ == "__main__":
    print(problem_0001())
