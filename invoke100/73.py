class Solution:
    def main(self,matrix):
        m = len(matrix[0])
        n = len(matrix)
        m_ = [False] * m
        n_ = [False] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    m_[j] = True
                    n_[i] = True
        for i in range(n):
            for j in range(m):
                if m_[j] or n_[i] == True:
                    matrix[i][j] = 0
        return matrix
s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(s.main(matrix))

