class Solution:
    def main(self,m,n):
        path = [[0] * m for _ in range(n)]
        for i in range(m):
            path[0][i] = 1
        for i in range(n):
            path[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                path[j][i] = path[j-1][i] + path[j][i-1]
        return path[n-1][m-1]
s = Solution()
print(s.main(3,7))
print(s.main(3,2))
