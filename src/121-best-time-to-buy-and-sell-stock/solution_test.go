// ref: https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMaxProfit(t *testing.T) {
	arrays := map[int][]int{
		9: {3, 4, 1, 6, 10, 5, 0},
		7: {3, 4, 4, 6, 10},
		0: {100, 97, 80, 64, 53, 27},
		4: {3, 7, 1, 3, 2, 5, 0},
	}
	t.Run("can get max forward diff of array values", func(t *testing.T) {
		for expected, array := range arrays {
			actual := MaxProfit(array)
			t.Log("Max (", array, ") is ", actual)
			msg := fmt.Sprintf("Expected MaxProfit to be %v", expected)
			require.Equal(t, expected, actual, msg)
		}
	})
}
