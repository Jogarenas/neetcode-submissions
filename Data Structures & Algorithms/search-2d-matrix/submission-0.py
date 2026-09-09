class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        row = 0
        while row < len(matrix):
            end = len(matrix[row]) - 1
            if matrix[row][end] == target:
                return True
            elif matrix[row][end] < target:
                row += 1
            elif (matrix[row][0] > target):
                return False
            else: 
                break
        
        if row == len(matrix):
            return False

        high = len(matrix[row]) - 1
        while l <= high:
            m = l + (high - l) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                l = m + 1
            if matrix[row][m] > target:
                high = m - 1
        return False