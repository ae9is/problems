// ref: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

package main

import (
	"fmt"
)

func isValid(s string) bool {
	// 1. Open brackets closed by same type of bracket
	// 2. Open brackets closed in correct order (same as 1.)
	// 3. Every close bracket has corresponding open bracket
	openStack := []rune{}
	for _, c := range s { // For char in string
		if _, ok := openBrackets[c]; ok {
			// Push open brackets onto a stack
			openStack = append(openStack, c)
		} else if _, ok := closeBrackets[c]; ok {
			// Handle close brackets
			if len(openStack) <= 0 {
				return false // 3.
			} else {
				// Pop last open bracket off the stack and compare to expected value given close bracket
				var last rune
				last, openStack = openStack[len(openStack)-1], openStack[:len(openStack)-1]
				openBracket := closeBrackets[c]
				if last != openBracket {
					return false // 1.
				}
			}
		}
	}
	return true
}

var openBrackets = map[rune]rune{
	'(': ')',
	'{': '}',
	'[': ']',
}
var closeBrackets = map[rune]rune{
	')': '(',
	'}': '{',
	']': '[',
}

func main() {
	fmt.Println(isValid("([{}]){()}"))
}
