class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        final = 0
        for char in operations:
            if char == "+":
                stack.append(stack[-1] + stack[-2])
            elif char == "D":
                stack.append(stack[-1] * 2)
            elif char == "C":
                stack.pop()
            else:
                stack.append(int(char))
        for val in stack:
            final += val
        return final