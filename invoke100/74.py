class Solution:
    def main(self,matrix,target):
        m = len(matrix[0])
        n = len(matrix)
        m_ = -1
        for i in range(n):
            min = matrix[i][0]
            max = matrix[i][-1]
            if target >= min and target <=max:
                m_ = i
                break
        if m_ != -1:
            left = 0
            right = n-1
            while left <= right:
                mid = (left + right)//2
                if target < matrix[m_][mid]:
                    right = mid - 1
                elif target > matrix[m_][mid]:
                    left = mid+1
                else:
                    return True

        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(s.main(matrix,target))
