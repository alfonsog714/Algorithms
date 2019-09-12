#!/usr/bin/python

import argparse


"""
Example case:
input of [1050, 270, 1540, 3800, 2] should return 3530 (why?)

1050:
--------
-1050 + 270 = -780
-1050 + 1540 = 490
-1050 + 3800 = 2750
-1050 + 2 = -1048


270:
-------
-270 + 1540 = 1270
-270 + 3800 = 3530
-270 + 2 = -268

1540:
-------
-1540 + 3800 = 2,260
-1540 + 2 = -1,538

"""
def find_max_profit(prices):
  # Example input: [1050, 270, 1540, 3800, 2]
  #                  0     1     2     3   4
  # Track the best profit so far
  max_profit_so_far = -20000
  for i in range(0, len(prices)):
    current_stock_price = prices[i]
    # print(f"Line 37: {current_stock_price}")
    for j in range(i + 1, len(prices)):
      # print(f"Line 39: {prices[j]}")
      if -current_stock_price + prices[j] > max_profit_so_far:
        max_profit_so_far = -current_stock_price + prices[j]
        # print(f"Line 42: {max_profit_so_far}")
  
  
  # print(f"End price: {max_profit_so_far}")
  return max_profit_so_far


# print(find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))