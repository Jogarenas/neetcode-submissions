class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        fin = []
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] in seen:
                nums.pop(i)
                l -= 1
            else:
                seen.setdefault(nums[i], 0)
                i += 1
     
        return len(nums)
