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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
