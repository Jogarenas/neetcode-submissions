class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        minVal = nums[0]
        l = 0
        r = len(nums) - 1
        return minVal
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < minVal:
                minVal = nums[m]
            elif nums[m] >= minVal:
                r = nums[m] - 1

        return minVal