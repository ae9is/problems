# ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    return max_pos_gradient(prices)


def max_pos_gradient(array: list[int]) -> int:
  """
  Get max single positive difference between values in array.
  Positive defined as from low -> high value i.e. forward difference.
  """
  max = 0
  for idx, a0 in enumerate(array):
    for a1 in array[idx:]:
      diff = a1 - a0
      if diff > max:
        max = diff
  return max


if __name__ == '__main__':
  a = [3, 4, 1, 6, 10, 5, 0]
  print(f'a: {a}')
  max = max_pos_gradient(a)
  print(f'max: {max}')
