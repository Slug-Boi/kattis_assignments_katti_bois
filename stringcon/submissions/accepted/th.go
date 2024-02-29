//usr/bin/gccgo 
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var input string
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		os.Exit(1)
	}
	lst := strings.Split(input, " ")

	fmt.Print(lst[0], lst[1], lst[2], lst[3])
}
