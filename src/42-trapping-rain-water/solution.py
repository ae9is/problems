# ref: https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
  def trap(self, height: List[int]) -> int:
    return trap(height)


def trap(height: list[int]) -> int:
  """
  Find area of troughs in a height map.

  We split the height map in two around the peak (any highest point).
  Then calculate the entrapped area for each uphill segment.
  """
  max_height = max(height)
  split_point = height.index(max_height)
  pre_split = height[:split_point + 1]  # Include peak in both halves
  post_split = height[split_point:]
  post_split_rev = list(reversed(post_split))
  total = trap_uphill(pre_split, max_height) + trap_uphill(post_split_rev, max_height)
  return total


def is_valid(height: list[int], threshold) -> bool:
  """
  Sanity check two properties:
  1. Height should not increase above max
  2. Height should end at or above start
  """
  start = height[0]
  end = height[-1]
  if end < start:
    return False
  max_height = max(height)
  if max_height > threshold:
    return False
  return True


def trap_uphill(height: list[int], threshold) -> int:
  """
  Find area of troughs in an increasing (uphill) height map.

  If the height map is not increasing, or passes a threshold, 
  then the area calculated after the heighest point will be incorrect.
  """
  if not is_valid(height, threshold):
    raise ValueError('Height map invalid')
  if not height:
    raise ValueError('Height required')
  pivot: int = height[0]
  trough_area = 0
  # For each point if height is increasing or flat set a new pivot,
  #  if height is decreasing then add trough area.
  for h in height:
    if h >= pivot:
      pivot = h
    else:
      diff = pivot - h
      trough_area += diff
  return trough_area


if __name__ == '__main__':
  a = [0,1,0,2,1,0,1,3,2,1,2,1]
  a_expect = 6
  b = [4,2,0,3,2,5]
  b_expect = 9
  for v, v_expect in [(a, a_expect), (b, b_expect)]:
    print(f'Height: {v}')
    print(f'Expected: {v_expect}')
    v_calc = trap(v)
    print(f'Calculated: {v_calc}')
