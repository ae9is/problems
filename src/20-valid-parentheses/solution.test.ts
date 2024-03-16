import { describe, expect, test } from '@jest/globals'
import { isValid } from './solution'

describe('20-valid-parentheses', () => {
  test('valid strings pass', () => {
    const validStrings = [
      '()',
      '()[]{}',
      '([{}]){()}',
      '[',
    ]
    for (const s of validStrings) {
      validate(s)
    }
  })
  test('invalid strings fail', () => {
    const invalidStrings = [
      '(]',
      '}',
      '[(]){}',
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
