class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for point in ops:
            if point == "+":
                if len(stack) >= 2:
                    score = stack[-1] + stack[-2]
                    stack.append(score)
            elif point == "D":
                score = 2 * stack[-1]
                stack.append(score) 
            elif point == "C":
                stack.pop()         
            else:
                point = int(point)
                stack.append(point)
        return sum(stack)
