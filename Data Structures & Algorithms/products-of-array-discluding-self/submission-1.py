class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        zerocount = 0
        maxval = 1
    

        for i in range(0,len(nums)):
            if nums[i] == 0:
                zerocount += 1
            else:
                maxval *= nums[i]

        for num in nums:
            if zerocount == 0:
                final.append(maxval//num)
            elif num != 0 and zerocount >= 1:
                final.append(0)
            elif num == 0 and zerocount == 1:
                final.append(maxval)
            else:
                final.append(0)

        return final