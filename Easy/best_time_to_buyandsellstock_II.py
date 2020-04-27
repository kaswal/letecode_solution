def buy_sell_stock_II(arr):
    max_profit = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_profit += arr[i] - arr[i - 1]

    return max_profit


input = [7, 1, 5, 3, 6, 4]

print(buy_sell_stock_II(input))
