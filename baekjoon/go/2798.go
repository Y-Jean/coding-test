// 브론즈 2. 블랙잭

// package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m int
	fmt.Fscanln(reader, &n, &m)

	var nums = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d ", &nums[i])
	}

	var sum int
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				val := nums[i] + nums[j] + nums[k]
				if nums[i] + nums[j] + nums[k] <= m && sum < val {
					sum = val
				} else {
					continue
				}
			}
		}
	}

	fmt.Println(sum)
}