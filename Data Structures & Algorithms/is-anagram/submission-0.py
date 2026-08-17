class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        let = {}
        for i in s:
            if i not in let:
                let[i] = 1
            else:
                let[i] += 1
        for j in t:
            if j not in let:
                let[j] = 1
            else:
                let[j] -= 1
        for key in let:
            if let[key] != 0:
                return False
        
        return True