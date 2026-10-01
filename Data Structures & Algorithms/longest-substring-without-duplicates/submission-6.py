class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxl = 0
        curl = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            maxl = max(maxl, right - left + 1)

        return max(maxl, curl)
           
               