// ref: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsValid(t *testing.T) {
	validStrings := [...]string{
		"()",
		"()[]{}",
		"([{}]){()}",
		"[",
	}
	invalidStrings := [...]string{
		"(]",
		"}",
		"[(]){}",
	}
	t.Run("valid strings validate", func(t *testing.T) {
		t.Log("Valid strings:")
		validate(validStrings[:], true, t)
	})
	t.Run("invalid strings invalidate", func(t *testing.T) {
		t.Log("Invalid strings:")
		validate(invalidStrings[:], false, t)
	})
}

func validate(strings []string, expected bool, t *testing.T) {
	for _, s := range strings {
		var status string
		valid := isValid(s)
		if valid {
			status = "valid"
		} else {
			status = "invalid"
		}
		t.Log(s, "is", status)
		msg := fmt.Sprintf("Expected isValid(%v) to be %v", valid, expected)
		require.Equal(t, valid, expected, msg)
	}
}
