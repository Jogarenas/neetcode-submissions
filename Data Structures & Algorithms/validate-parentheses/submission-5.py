class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")":"(", "}":"{","]":"["}
        for char in s:
            if (len(s) % 2) != 0:
                return False

            if char in [")",'}',"]"] and len(stack) == 0:
                return False

            if char in ["(","{","["]:
                stack.append(char)
                print(stack)

            elif (char in [")",'}',"]"]) and (stack[-1] == matches[char]):
                stack.pop()

            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
