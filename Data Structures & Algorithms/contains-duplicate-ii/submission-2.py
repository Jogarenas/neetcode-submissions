class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #size of nums
        n = len(nums)
        for i in range(n):
            curCheck = nums[i: i + k +1 ]
            curSet = set(curCheck)
            if len(curCheck) != len(curSet):
                return True
        return False