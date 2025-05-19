class Solution:
    def isValidSudoku(self, nums) ->bool:
        row = [[0 for i in range(9)] for i in range(9)]
        col = [[0 for i in range(9)] for i in range(9)]
        subbox = [[[0 for i in range(9)] for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if nums[i][j] !='.':
                    index = int(nums[i][j]) - 1
                    row[i][index] +=1
                    col[j][index] += 1
                    subbox[i//3][j//3][index] += 1
                    if row[i][index] > 1 or col[j][index] > 1 or subbox[i//3][j//3][index] > 1:
                        return False
        return True


s = Solution()
nums = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '6', '8', '.', '.', '.', '.', '5', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '3', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]
print(s.isValidSudoku(nums))