// Check whether a sudoku board is valid.
// Written to work with arbitrary sudoku size like 1x1, 4x4, 9x9, 16x16, 25x25, etc.
// (Won't pass weird boards like 10x10.)
//
// ref: https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150

package main

import (
	"fmt"
	"math"
)

// Just to match the online problem given, at least a couple things are non-ideal:
// - byte used instead of rune (there's no reason a sudoku couldn't have arbitrary non-digit symbols)
// - No reason is returned as for why validation fails
func isValidSudoku(board [][]byte) bool {
	if !checkLegalBoardSize(board) || !checkRowsValid(board) {
		return false
	}
	transpose := transpose(board)
	if !checkRowsValid(transpose) {
		return false
	}
	sections := section(board)
	if !checkRowsValid(sections) {
		return false
	}
	_ = 0
	return true
}

func checkLegalBoardSize(board [][]byte) bool {
	size := len(board)
	// Check size > 0
	if size <= 0 {
		fmt.Println("No board")
		return false
	}
	// Check N has integer square root
	sqrt := math.Sqrt(float64(size))
	if math.Trunc(sqrt) != sqrt {
		fmt.Println("Board size not a squared integer")
		return false
	}
	// Check board is N x N
	for _, row := range board {
		if len(row) != size {
			fmt.Println("Board not square")
			return false
		}
	}
	return true
}

func checkRowsValid(board [][]byte) bool {
	for _, row := range board {
		colValues := make(map[byte]struct{})
		numUndef := 0
		for _, val := range row {
			if val != '.' {
				colValues[val] = struct{}{}
			} else {
				numUndef++
			}
		}
		// Check number unique defined values against expected size, accounting for undefined '.' values
		if len(colValues)+numUndef < len(row) {
			return false
		}
	}
	return true
}

func transpose(board [][]byte) (transpose [][]byte) {
	// Preallocate new 2D slice
	numColsMax := 0
	for _, row := range board {
		if len(row) > numColsMax {
			numColsMax = len(row)
		}
	}
	numRows := len(board)
	transpose = make([][]byte, numColsMax)
	for i := range board {
		transpose[i] = make([]byte, numRows)
	}
	// Transpose
	for i, row := range board {
		for j, val := range row {
			transpose[j][i] = val
		}
	}
	return transpose
}

// Section N x N sudoku board into squares of size n x n, n = sqrt(N).
// Return the pieces as a list of 1D slices of size N.
func section(board [][]byte) (sections [][]byte) {
	N := len(board)
	n := int(math.Sqrt(float64(N)))
	sections = make([][]byte, N)
	for i := 0; i < N; i += n {
		relevantRows := board[i : i+n]
		for j := 0; j < N; j += n {
			for _, row := range relevantRows {
				relevantCols := row[j : j+n]
				sectionNum := (i*n + j) / n
				sections[sectionNum] = append(sections[sectionNum], relevantCols...)
			}
		}
	}
	return sections
}

func main() {
	board1 := [][]byte{
		{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	board2 := [][]byte{
		{'8', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}
	board3 := [][]byte{
		{'a', 'b', 'c', 'd'},
		{'c', 'd', '.', 'b'},
		{'b', 'a', 'd', 'c'},
		{'d', 'c', 'b', 'a'},
	}
	boards := [][][]byte{board1, board2, board3}
	for idx, board := range boards {
		var valid string
		if isValidSudoku(board) {
			valid = ""
		} else {
			valid = " not"
		}
		fmt.Printf("Board %v is%v a valid sudoku\n", idx, valid)
	}
}
