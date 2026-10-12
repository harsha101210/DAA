def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    used = [0] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used[i] = coin

    result = []
    current = amount

    while current > 0:
        result.append(used[current])
        current -= used[current]

    return dp[amount], result


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

minimum, coins_used = coin_change(coins, amount)

print("Minimum coins required:", minimum)
print("Coins used:", coins_used)
