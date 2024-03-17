from solution import Solution


def test_20():
  print('Running test_20 ...')
  validStrings = [
    '()',
    '()[]{}',
    '([{}]){()}',
    '[',
  ]
  invalidStrings = [
    '(]',
    '}',
    '[(]){}',
  ]
  for s in validStrings:
    validate(s)
  for s in invalidStrings:
    validate(s, False)


def validate(string: str, outcome=True):
  valid = Solution().isValid(string)
  print(f'{string} is {"valid" if valid else "invalid"}')
  if outcome:
    assert valid
  else:
    assert not valid


if __name__ == '__main__':
  test_20()
