// ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

package main

import "fmt"

func MaxProfit(prices []int) int {
	return maxPosGradient(prices)
}

// Get max single positive difference between values in array.
// Positive defined as from low -> high value i.e. forward difference.
func maxPosGradient(array []int) (max int) {
	for idx, a0 := range array {
		for _, a1 := range array[idx:] {
			diff := a1 - a0
			if diff > max {
				max = diff
			}
		}
	}
	return max
}

func main() {
	a := []int{3, 4, 1, 6, 10, 5, 0}
	fmt.Println("a:", a)
	max := MaxProfit(a)
	fmt.Println("max:", max)
}
