import { describe, expect, test } from '@jest/globals'
import { isPalindrome as isValid } from './solution'

describe('125-valid-palindrome', () => {
  test('valid strings pass', () => {
    const validStrings = [
      'a man, a plan, a canal: panama',
      ' ',
    ]
    for (const s of validStrings) {
      validate(s)
    }
  })
  test('invalid strings fail', () => {
    const invalidStrings = [
      'race a car',
    ]
    for (const s of invalidStrings) {
      validate(s, false)
    }
  })
})

function validate(str: string, outcome = true) {
  const valid = isValid(str)
  console.log(str + ' is ' + (valid ? 'valid' : 'invalid'))
  if (outcome) {
    expect(valid).toBeTruthy()
  } else {
    expect(valid).toBeFalsy()
  }
}
