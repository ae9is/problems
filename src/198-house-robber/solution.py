# ref: https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150

from typing import List
import copy

DEBUG = False


class Solution:
  def rob(self, nums: List[int]) -> int:
    return solve(nums)


def solve(nums: list[int]) -> int:
  """
  A brute force solution checking all the possible outcomes.
  """
  return find_max(0, nums, [])


def find_max(i: int, nums: list[int], branch: list[int]):
  if i >= len(nums):
    # If we've reached the end of our array find out the max value from our branches
    branch_sum = sum(branch)
    if DEBUG:
      print(f'i: {i}, sum: {branch_sum}, branch: {branch}')
    return branch_sum

  # Add next value onto branches
  branch_picking_next = None
  if i + 1 < len(nums):
    # Only pick next if next is valid
    branch_picking_next = copy.deepcopy(branch)
    branch_picking_next.append(nums[i + 1])
  branch_picking_current = branch
  branch_picking_current.append(nums[i])

  # Recurse and join the results of the recursion
  max_picking_current = find_max(i + 2, nums, branch_picking_current)
  max_picking_next = find_max(i + 3, nums, branch_picking_next) if branch_picking_next else 0
  if max_picking_next > max_picking_current:
    return max_picking_next
  return max_picking_current


if __name__ == '__main__':
  a = [7, 9, 3, 1, 6, 1]  # 16
  print('a: ', a)
  max_sum = solve(a)
  print('max: ', max_sum)
