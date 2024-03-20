from solution import Solution


def test():
  tests = [
    (False, 'a', 'b'),
    (False, 'aa', 'ab'),
    (True, 'aa', 'aab'),
    (True, 'toils', 'solution'),
    (False, 'iota', 'solution'),
  ]
  for expected, ransomNote, magazine in tests:
    calc = Solution.canConstruct(expected, ransomNote, magazine)
    print(f'Expected: {expected}, Calculated: {calc}')
    assert expected == calc
  print(f'All {len(tests)} tests passed.')


if __name__ == '__main__':
  test()
