// ref: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
//
// The problem as worded is ambigious and this solution assumes:
// a) Nested brackets i.e. ([{}]){()} are valid
// b) Open brackets do not need to be closed
//
// Rule "Open brackets must be closed in the correct order" is also vague.
// Here we redefine as "Children of open brackets must be closed first before their parent."
//
// Stylistically, this solution is written as a collection of arbitrary and separate rules, not for efficiency.


function isValid(s: string): boolean {
  if (
    // onlyContainsBrackets(s) && 
     openBracketsClosedBySameType(s)
     && openBracketsClosedInCorrectOrder(s)
     && closeBracketsHaveOpenBrackets(s)
  ) {
    return true
  }
  return false
}

class Bracket {
  open: string
  close: string

  constructor(open: string, close: string) {
    this.open = open
    this.close = close
  }
}

const validBrackets: Bracket[] = [
  new Bracket('(', ')'),
  new Bracket('{', '}'),
  new Bracket('[', ']'),
]
const validCharacters: string[] = validBrackets.flatMap((b: Bracket) => {
  return [b.open, b.close]
})
console.log('Valid characters: ', validCharacters)
const validOpenBrackets = validBrackets.map((b: Bracket) => b.open)
const validCloseBrackets = validBrackets.map(b => b.close)
const correspondingBracket = new Map<string, string>()
for (const b of validBrackets) {
  correspondingBracket.set(b.open, b.close)
  correspondingBracket.set(b.close, b.open)
}
console.log('Bracket pairings:\n', [...correspondingBracket.entries()])

// function onlyContainsBrackets(s: string) {
//   for (const c of s) {
//     if (!(validCharacters.includes(c))) {
//       return false
//     }
//   }
//   return true
// }

function openBracketsClosedBySameType(s: string) {
  /**
   * Rule: Open brackets must be closed by the same type of brackets.
   */
  const openStack: string[] = []
  for (const c of s) {
    if (validOpenBrackets.includes(c)) {
      openStack.push(c)
    } else if (validCloseBrackets.includes(c)) {
      if (openStack.length <= 0) {
        // We have an extra closing bracket, which for this rule specifically is okay.
      } else {
        const last = openStack.pop()
        const openBracket = correspondingBracket.get(c)
        if (last !== openBracket) {
          return false
        }
      }
    }
  }
  return true
}

function openBracketsClosedInCorrectOrder(s: string) {
  /**
   * Rule: Open brackets must be closed in the correct order.
   * 
   * Which is completely arbitary since "the correct order" is undefined, 
   * and so we've redefined to mean:
   * "Children of open brackets must be closed first before their parent."
   * 
   * i.e. ([{}]){()} 
   * 
   * This is functionally the same as openBracketsClosedBySameType.
   */
  return openBracketsClosedBySameType(s)
}
 
function closeBracketsHaveOpenBrackets(s: string) {
  /**
   * Rule: Every close bracket has a corresponding open bracket of the same type.
   * 
   * Check that number of close and open brackets of each type is the same.
   */
  const bracketCounts: Map<string, number> = new Map()
  for (const c of validCharacters) {
    bracketCounts.set(c, 0)
  }
  for (const c of s) {
    if (validCharacters.includes(c)) {
      bracketCounts.set(c, (bracketCounts.get(c) ?? 0) + 1)
    }
  }
  for (const c of validCloseBrackets) {
    // In this solution we only validate if close brackets have open brackets,
    //  not if open brackets have close brackets.
    if (s.includes(c)) {
      const numClose = bracketCounts.get(c)
      const openBracket = correspondingBracket.get(c)
      const numOpen = bracketCounts.get(openBracket ?? '') || 0
      if (numClose !== numOpen) {
        return false
      }
    }
  }
  return true
}

export { isValid }
