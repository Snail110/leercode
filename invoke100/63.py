class Solution:
    def main(self,obstaclegrid):
        m = len(obstaclegrid[0])
        n = len(obstaclegrid)
        path = [[0] * m for _ in range(n)]
        for i in range(m):
            path[0][i] = 1
        for j in range(n):
            path[j][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                if obstaclegrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        return path[n-1][m-1]

s = Solution()
obstaclegrid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.main(obstaclegrid))           