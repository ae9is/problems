# ref: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
#
# The problem as worded is ambigious and this solution assumes:
# a) Nested brackets i.e. ([{}]){()} are valid
# b) Open brackets do not need to be closed
#
# Rule "Open brackets must be closed in the correct order" is also vague.
# Here we redefine as "Children of open brackets must be closed first before their parent."
#
# Stylistically, this solution is written as a collection of arbitrary and separate rules, not for efficiency.

import functools


class Solution:
  def isValid(self, s: str) -> bool:
    if (
      #onlyContainsBrackets(s) and
      openBracketsClosedBySameType(s)
      and openBracketsClosedInCorrectOrder(s)
      and closeBracketsHaveOpenBrackets(s)
    ):
      return True
    return False


class Bracket:
  open: str
  close: str

  def __init__(self, open: str, close: str):
    self.open = open
    self.close = close


validBrackets = [
  Bracket('(', ')'),
  Bracket('{', '}'),
  Bracket('[', ']'),
]
validCharacters = functools.reduce(lambda x, y: x + y, [[b.open, b.close] for b in validBrackets])
validOpenBrackets = [b.open for b in validBrackets]
validCloseBrackets = [b.close for b in validBrackets]
correspondingBracket: dict[str, str] = {
  b.open: b.close for b in validBrackets
} | {
  b.close: b.open for b in validBrackets
}


## Implicit constraint
# def onlyContainsBrackets(s):
#  for c in s:
#    if c not in validCharacters:
#      return False
#  return True


def openBracketsClosedBySameType(s):
  """
  Rule: Open brackets must be closed by the same type of brackets.
  """
  openStack = []
  for c in s:
    if c in validOpenBrackets:
      openStack.append(c)
    elif c in validCloseBrackets:
      if len(openStack) <= 0:
        # We have an extra closing bracket, which for this rule specifically is okay.
        pass
      else:
        last = openStack.pop()
        openBracket = correspondingBracket[c]
        if last != openBracket:
          return False
  return True


def openBracketsClosedInCorrectOrder(s):
  """
  Rule: Open brackets must be closed in the correct order.

  Which is completely arbitary since "the correct order" is undefined, 
  and so we've redefined to mean:
  "Children of open brackets must be closed first before their parent."

  i.e. ([{}]){()} 

  This is functionally the same as openBracketsClosedBySameType.
  """
  return openBracketsClosedBySameType(s)


def closeBracketsHaveOpenBrackets(s):
  """
  Rule: Every close bracket has a corresponding open bracket of the same type.

  Check that number of close and open brackets of each type is the same.
  """
  bracketCounts: dict[str, int] = {
    c: 0 for c in validCharacters
  }
  for c in s:
    if c in validCharacters:
      bracketCounts[c] += 1
  for c in validCloseBrackets:
    # In this solution we only validate if close brackets have open brackets,
    #  not if open brackets have close brackets.
    if c in s:
      numClose = bracketCounts[c]
      openBracket = correspondingBracket[c]
      numOpen = bracketCounts[openBracket]
      if numClose != numOpen:
        return False
  return True


if __name__ == '__main__':
  print(f'Bracket pairings: {correspondingBracket}')
