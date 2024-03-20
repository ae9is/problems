from solution import Solution


def test():
  tests = [
    (0, 0, [7,1,5,3,6,4]), 
    (1, 5, [7,1,5,3,6,4]), 
    (2, 7, [7,1,5,3,6,4]), 
    (2, 4, [1,2,3,4,5]),
    (2, 0, [7,6,4,3,1]),
    (2, 10, [3, 4, 1, 6, 10, 5, 0]),
    (2, 2, [2,4,1]),
    (2, 7, [3,2,6,5,0,3]),
    (2, 12, [2, 4, 1, 6, 10, 5, 8]),
    (3, 14, [2, 4, 1, 6, 10, 5, 8]),
  ]
  for k, expected, prices in tests:
    calc = Solution().maxProfit(k=k, prices=prices)
    print(f'Expected: {expected}, Calculated: {calc}')
    assert expected == calc
  print(f'All {len(tests)} tests passed.')


if __name__ == '__main__':
  test()
