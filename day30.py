coins = list(map(int, input("Enter coin denominations separated by space: ").split()))
amount = int(input("Enter the amount: "))
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for c in coins:
        if c <= i:
            dp[i] = min(dp[i], dp[i - c] + 1)
print(-1 if dp[amount] > amount else dp[amount])