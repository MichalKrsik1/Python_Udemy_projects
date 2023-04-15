def return_change(payment=288, cost=100):
    coins = [50, 20, 10, 5, 2, 1]
    coin_count = []

    if cost > payment:
        return "Not enough money"

    change = (payment - cost) % 100

    for coin in coins:
        count, change = divmod(change, coin)
        coin_count.append(f"{count}x")

    dic_coins = {coins[i]: coin_count[i] for i in range(len(coins))}

    return f"Change: {payment - cost}\nChange in coins: {(payment - cost) % 100}\nCoins needed: {dic_coins}"

print(return_change())