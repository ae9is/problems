from solution import Solution


def test():
  tests = [
    (9, [3, 4, 1, 6, 10, 5, 0]),
    (7, [3, 4, 4, 6, 10]),
    (0, [100, 97, 80, 64, 53, 27]),
    (4, [3, 7, 1, 3, 2, 5, 0]),
  ]
  for expected, array in tests:
    calc = Solution().maxProfit(array)
    assert expected == calc
    print(f'Expected: {expected}, Calculated: {calc}')
  print('All tests passed.')


if __name__ == '__main__':
  test()
