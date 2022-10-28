"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2 解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
向右 -> 向右 -> 向下 -> 向下
向下 -> 向下 -> 向右 -> 向右

动规五部曲：

1.确定dp数组（dp table）以及下标的含义
dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。

2.确定递推公式
递推公式和62.不同路径一样，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。

但这里需要注意一点，因为有了障碍，(i, j)如果就是障碍的话应该就保持初始状态（初始状态为0）。

所以代码为：
if (obstacleGrid[i][j] == 0) { // 当(i, j)没有障碍的时候，再推导dp[i][j]
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
}
3.dp数组如何初始化
vector<vector<int>> dp(m, vector<int>(n, 0));
for (int i = 0; i < m && obstacleGrid[i][0] == 0; i++) dp[i][0] = 1;
for (int j = 0; j < n && obstacleGrid[0][j] == 0; j++) dp[0][j] = 1;

4.确定遍历顺序
从递归公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 中可以看出，一定是从左到右一层一层遍历，这样保证推导dp[i][j]的时候，dp[i - 1][j] 和 dp[i][j - 1]一定是有数值。

5.举例推导dp数组
"""

class Solution:
    def maxPath(self,obstacleGrid:list):
        m = len(obstacleGrid) # 行
        n = len(obstacleGrid[0]) # 竖

        # 确定dp
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化 dp
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1

        # 递推公式 遍历
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

s = Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

print(s.maxPath(obstacleGrid))