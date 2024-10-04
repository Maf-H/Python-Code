"""A function tries to buy at small and sell at large prices and return it else returns 0"""
def max_profit(prices: list[int]) -> int:
    """
    compare current price with the price you buy:
        if current price is greater than you buy:
            try to sell it and compare your profit with previos profit
        else:
            update buying price to the current price 
    1st. Method 
    Time Complexity O(n^2)
    Space Complexity O(1)

    2nd. Method
    Time Complexity O(n)
    Space Complexity O(1)
    """
    profit = 0
    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         curr = prices[j] - prices[i]
    #         if curr > max_profit:
    #             max_profit = curr
    # return max_profit



    buy = prices[0]
    for price in prices[1:]:
        if price > buy:
            profit = max(profit, (price - buy))
        elif price < buy:
            buy = price
    return profit
    # if we don't need the index it is recommended to use "in prices[1:]" instead of range
a = [7,1,5,3,6,4]
print(max_profit(a))
