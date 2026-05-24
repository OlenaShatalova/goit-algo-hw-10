from timeit import timeit

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    """Жадібний алгоритм: завжди бере найбільшу можливу монету."""
    result = {}
    for coin in sorted(coins, reverse=True):
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    """Динамічне програмування: знаходить мінімальну кількість монет."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    result = {}
    while amount > 0:
        for coin in coins:
            if coin <= amount and dp[amount - coin] == dp[amount] - 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break

    return dict(sorted(result.items()))


# Тест
amount = 113
print(f"Сума: {amount}")
print(f"Жадібний:  {find_coins_greedy(amount)}")
print(f"Динамічне: {find_min_coins(amount)}")

# Порівняння часу виконання
big_amount = 99999

greedy_time = timeit(lambda: find_coins_greedy(big_amount), number=100)
dp_time = timeit(lambda: find_min_coins(big_amount), number=100)

print(f"\nЧас для суми {big_amount} (100 запусків):")
print(f"Жадібний:         {greedy_time:.6f} сек")
print(f"Динамічне прогр.: {dp_time:.6f} сек")