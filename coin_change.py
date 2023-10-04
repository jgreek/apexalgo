def coinChange(coins, amount):
    # Create the dp table and initialize with 'inf'. Size is (amount + 1) to cover all amounts from 0 to amount.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: 0 amount requires 0 coins

    # For each coin, update dp table for all amounts from coin value to amount
    for coin in coins:
        for i in range(coin, amount + 1):
            # Update the current amount's value with the minimum of current value and (value of (current amount - coin) + 1)
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still 'inf', amount can't be formed by given coins
    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
print(coinChange([1, 2, 5], 11))  # Expected output: 3
print(coinChange([2], 3))  # Expected output: -1
print(coinChange([1], 0))  # Expected output: 0
