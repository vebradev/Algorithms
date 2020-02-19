#!/usr/bin/python

import argparse

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

# print(find_max_profit(stocks)) # => 6
# print(find_max_profit(stocks2)) # => -10

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
