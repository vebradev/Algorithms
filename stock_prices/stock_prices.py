#!/usr/bin/python

import argparse

# For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices,
# but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it;
# it can't come after it in the list of prices.

# So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?

# input  [10, 7, 5, 8, 11, 9]
# output 6
stocks = [10, 7, 5, 8, 11, 9]
stocks2 = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
    # set some defaults
    lowest = prices[0]
    profits = []
    # 1. iterate over the list of stock prices starting at index 1
    for i in range(1, len(prices)):
        # grab current index and the previous one
        current, previous = prices[i], prices[i - 1]
        # find the lowest by comparing defaut lowest & previous index
        lowest = min(lowest, previous)
        # calculate the difference and append it to profits list
        profit = current - lowest
        profits.append(profit)
    return max(profits)

print(find_max_profit(stocks)) # => 6
print(find_max_profit(stocks2)) # => -10

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
