class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxcons = 0

        for num in nums:
            if num -1 not in nums:
                curcons = 1

                while num + curcons in nums:
                    curcons += 1

                maxcons = max(maxcons, curcons)
        else:
            return maxcons