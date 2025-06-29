#!/usr/bin/python3
"""Prime numbers game"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game over x eounds.

    Args:
        x (int): number of rounds
        nums (list): list of integers

    Returns:
        str: the name of player who won most rounds
    """

    if not nums or x < 1:
        return None

    max_n = max(nums)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, max_n + 1, i):
                is_prime[multiple] = False

    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        prime_count = prime_counts[n]

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
