def buyandsellstock(arr):
    min_buy_price = arr[0]
    current_max_profit = 0

    for i in range(1, len(arr)):
        if arr[i] < min_buy_price:
            min_buy_price = arr[i]

        else:
            max_profit = arr[i] - min_buy_price
            if max_profit > current_max_profit:
                current_max_profit = max_profit

    return current_max_profit


input = [7,1,5,3,6,4]

print(buyandsellstock(input))
