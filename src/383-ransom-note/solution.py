# ref: https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150


class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    return canConstruct(ransomNote, magazine)


def canConstruct(ransomNote: str, magazine: str) -> bool:
  print(f'Note: {ransomNote}, Magazine: {magazine}')
  char_stack = list(magazine)
  for char in ransomNote:
    try:
      idx = char_stack.index(char)
      char_stack.pop(idx)
      print(f'Magazine: {"".join(char_stack)}')
    except ValueError:
      return False
  return True


if __name__ == '__main__':
  calc = canConstruct('baa', 'banana')
  print(f'canConstruct: {calc}')
