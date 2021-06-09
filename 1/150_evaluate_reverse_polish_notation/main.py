class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                r, l = int(stack.pop()), int(stack.pop())
                if token == "+":
                    stack.append(l + r)
                elif token == "-":
                    stack.append(l - r)
                elif token == "*":
                    stack.append(l * r)
                else:
                    stack.append(l / r)
        return int(stack.pop())


if __name__ == '__main__':
    s = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    assert s.evalRPN(tokens) == 9

    tokens = ["4", "13", "5", "/", "+"]
    assert s.evalRPN(tokens) == 6

    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    assert s.evalRPN(tokens) == 22
