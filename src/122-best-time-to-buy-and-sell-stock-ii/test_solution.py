from solution import Solution


def test():
  tests = [
    (7, [7,1,5,3,6,4]), 
    (4, [1,2,3,4,5]),
    (0, [7,6,4,3,1]),
    (10, [3, 4, 1, 6, 10, 5, 0]),
    (0, [-3]),
    (10, [-7,-1,-5,-3,-6,-4]), 
  ]
  for expected, array in tests:
    calc = Solution().maxProfit(array)
    print(f'Expected: {expected}, Calculated: {calc}')
    assert expected == calc
  print('All tests passed.')


if __name__ == '__main__':
  test()
