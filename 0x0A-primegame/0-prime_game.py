#!/usr/bin/python3
""" Check winner of a game """


def isWinner(x, nums):
    """ Check winner of a game """
    if x < 1 or not nums:
        return None

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes_count = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if primes[i]:
            count += 1
            primes_count[i] = count
    print(primes_count)
    player = 0
    for i in nums:
        player ^= primes_count[i] % 2

    return "Maria" if player else "Ben"
