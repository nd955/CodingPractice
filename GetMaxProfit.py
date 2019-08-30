import math

def get_max_profit(stock_prices_yesterday):
    max_difference = -math.inf
    curr_min = math.inf

    for i in range(len(stock_prices_yesterday)):
        if stock_prices_yesterday[i] - curr_min > max_difference:
            max_difference = stock_prices_yesterday[i] - curr_min
        if stock_prices_yesterday[i] < curr_min:
            curr_min = stock_prices_yesterday[i]

    return max_difference

stock_prices_yesterday = [10, 70]

print(get_max_profit(stock_prices_yesterday))