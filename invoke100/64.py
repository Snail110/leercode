class Solution:
    def main(self,grid):
        m = len(grid[0])
        n = len(grid)
        path_sum_min = [[0] * m for _ in range(n)]
        path_sum_min[0][0] = grid[0][0]
        for i in range(m):
            path_sum_min[0][i] = sum(grid[0][0:i+1])
        for j in range(1,n):
            path_sum_min[j][0] = path_sum_min[j-1][0] + grid[j][0]
        
        for i in range(1,n):
            for j in range(1,m):
             path_sum_min[i][j] = min(path_sum_min[i-1][j],path_sum_min[i][j-1]) + grid[i][j]
        
        return path_sum_min[n-1][m-1]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(s.main(grid))
