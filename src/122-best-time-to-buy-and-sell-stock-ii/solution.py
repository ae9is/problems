# ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """
    Problem:
      Can buy one stock at once, any number of transactions.
      Given array of prices[i] of stock on i-th day. Find max profit.

    This function starts at the last day and works backwards
      to calculate max future profits from that day.
    """
    # Max profit from day i, for convenience in a map instead of writing an array in reverse
    N = len(prices) - 1
    max_profit_from_day = {N: 0}
    # Starting from the second last day and working towards the first,
    #  calculate the future profits possible from each day
    for i in range(1, N + 1):
      future_profits = [0]
      for j in range(0, i):
        # The future possible profit depends on how long we hold onto a buy on the current day,
        #  and the max profit from our sell date
        profit_with_buy = prices[N - j] - prices[N - i] + max_profit_from_day[N - j]
        profit_without_buy = max_profit_from_day[N - j]
        future_profits.extend([profit_with_buy, profit_without_buy])
      max_profit_from_day[N - i] = max(future_profits)
    max_profit = max(max_profit_from_day.values())
    return max_profit


if __name__ == '__main__':
  a = [3, 4, 1, 6, 10, 5, 0]
  print(f'a: {a}')
  max = Solution().maxProfit(a)
  print(f'max: {max}')
