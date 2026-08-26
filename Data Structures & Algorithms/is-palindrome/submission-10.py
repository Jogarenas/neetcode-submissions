class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0
        s=s.lower()
        s="".join([char for char in s if char.isalnum()])
        backward = len(s) - 1
        while forward < len(s):

            if s[forward] != s[backward]:
                return False
            forward += 1
            backward -= 1

        return True