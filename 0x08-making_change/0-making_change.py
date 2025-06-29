#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to get a given amt.

    Args:
        coins (list): List of the value of the coins in possesion
        total (int): The target amount to meet.

    Returns:
        int: Fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0

    coins.sort()

    max_coins_needed = total + 1

    dp = [max_coins_needed] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break

            if dp[i - coin] != max_coins_needed:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != max_coins_needed else -1
