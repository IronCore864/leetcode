package main

import (
	"fmt"
	"strconv"
)

func helper(res []string, path string, num string, target int64, pos int, eval int64, multi int64) []string {
	if pos == len(num) {
		if target == eval {
			res = append(res, path)
		}
		return res
	}

	for i := pos; i < len(num); i += 1 {
		if i != pos && string(num[pos]) == "0" {
			break
		}

		cur, _ := strconv.ParseInt(num[pos:i+1], 10, 64)

		if pos == 0 {
			res = helper(res, path+strconv.Itoa(int(cur)), num, target, i+1, cur, cur)
		} else {
			res = helper(res, path+"+"+strconv.Itoa(int(cur)), num, target, i+1, eval+cur, cur)
			res = helper(res, path+"-"+strconv.Itoa(int(cur)), num, target, i+1, eval-cur, -cur)
			res = helper(res, path+"*"+strconv.Itoa(int(cur)), num, target, i+1, eval-multi+multi*cur, multi*cur)
		}

	}
	return res
}

func addOperators(num string, target int) []string {
	var res []string
	if num == "" {
		return res
	}
	t := int64(target)
	res = helper(res, "", num, t, 0, 0, 0)
	return res
}

func main() {
	fmt.Println(addOperators("105", 5))
}
