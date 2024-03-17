// ref: https://go.dev/tour/moretypes/26
package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	prev := 0
	current := 1
	first := true
	return func() int {
		if first {
			first = false
			return 0
		}
		next := prev + current
		prev = current
		current = next
		return prev
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
