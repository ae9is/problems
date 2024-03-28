from solution import Solution


def test():
  tests = [
    (4, [1, 2, 3, 1]),
    (12, [2, 7, 9, 3, 1]),
    (16, [7, 9, 3, 1, 6, 1]),
    (12, [3, 2, 6, 5, 0, 3]),
    (22, [2, 4, 1, 6, 10, 5, 8]),
    (5, [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0]),
    (0, []),
    (10, [1]*20),
  ]
  for expected, nums in tests:
    calc = Solution().rob(nums)
    print(f'Expected: {expected}, Calculated: {calc}')
    assert expected == calc
  print(f'All {len(tests)} tests passed.')


if __name__ == '__main__':
  test()
