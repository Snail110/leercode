class Solution:
    def rotate(self,matrix):
        ll = len(matrix[0])
        for j in range(ll):
            for i in range(j,ll):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp
        for j in range(0,ll//2):
            for i in range(ll):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][ll-1-j]
                matrix[i][ll-1-j] = tmp

        return matrix

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(s.rotate(matrix))