// ref: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

export function isPalindrome(s: string): boolean {
  console.log('Input: ' + s)
  const norm = s.toLowerCase().replaceAll(/s+/g, '').replaceAll(/[^a-z0-9]/g, '')
  console.log('Normalised: ' + norm)
  const reverse = [...norm].reverse().join('')
  console.log('Reversed: ' + reverse)
  return norm === reverse
}

console.log(isPalindrome('a man, a plan, a canal: panama'))
console.log(isPalindrome('race a car'))
console.log(isPalindrome(' '))
