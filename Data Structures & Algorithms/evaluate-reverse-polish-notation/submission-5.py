class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        curval = 0
        for char in tokens:
            if char in operators:
                if char == "+":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    val = int(first + second)
                    stack.append(val)
                if char == "-":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    val = int(second - first)
                    stack.append(val)
                if char == "*":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    val = int(first * second)
                    stack.append(val)
                if char == "/":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    val = int(second / first)
                    stack.append(val)
            else:
                stack.append(int(char))

        return stack.pop()