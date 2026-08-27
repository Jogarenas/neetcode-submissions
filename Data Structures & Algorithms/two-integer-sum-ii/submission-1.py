class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while first != len(numbers) and second > 0:
            s = numbers[first] + numbers[second]
            if s == target:
                return [first + 1, second + 1]
            if s < target:
                first += 1
            if s > target:
                second -= 1
            

