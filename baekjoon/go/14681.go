// 브론즈 5. 사분면 고르기

package main

import "fmt"

func main() {
	var a, b int

	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)

	if a > 0 && b > 0 {
		fmt.Println("1")
	} else if a < 0 && b > 0 {
		fmt.Println("2")
	} else if a < 0 && b < 0 {
		fmt.Println("3")
	} else if a > 0 && b < 0 {
		fmt.Println("4")
	}
}