from solution import Solution


def test():
  example_height = [0,1,0,3,1,0,1,3,2,1,2,1]
  tests = [
    (6, [0,1,0,2,1,0,1,3,2,1,2,1]),
    (9, [4,2,0,3,2,5]),
    (0, [0,2,0]),
    (1, [0,-1,0,1]),
    (0, [5]),
    (9, example_height),
    (3*9, [3*i for i in example_height]),
  ]
  for expected, height in tests:
    calc = Solution().trap(height)
    print(f'Expected: {expected}, Calculated: {calc}')
    assert expected == calc
  print(f'All {len(tests)} tests passed.')


if __name__ == '__main__':
  test()
