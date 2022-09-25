"""
二维数组路径最小和，并且求的最小路径
"""

# 动态规划
class Solution:
    def minPath(self,nums:list):
        # 初始化
        m = len(nums)
        n = len(nums[0])
        # 定义 dp[i][j] 为从左上角走到ij的位置，最小路径总和
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化 00
        dp[0][0] = nums[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + nums[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + nums[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j] + nums[i][j],dp[i][j-1] + nums[i][j])

        return dp

# 回溯方法
class Solution1:
    def __init__(self):
        self.minvalue = 2 ** 64 - 1
        self.res = []
    def minSumPath(self,nums):
        # 初始化
        m = len(nums)
        n = len(nums[0])
        path = []
        val = nums[0][0]
        path.append([0,0])
        def dsp(i,j,path:list,val:int):
            # 终止条件
            if i == m-1 and j == n-1:
                if self.minvalue > val:
                    self.minvalue = val
                    self.res = path[:]
                    return
            if i + 1 < m:
                i = i + 1
                val += nums[i][j]
                path.append([i,j])
                dsp(i,j,path,val)
                val -= nums[i][j]
                i = i - 1
                path.pop()
            if j + 1 < n:
                j = j + 1
                val += nums[i][j]
                path.append([i,j])
                dsp(i,j,path,val)
                val -= nums[i][j]
                j = j - 1
                path.pop()

        dsp(0,0,path,val)
        return self.res,self.minvalue

# s = Solution()
nums = [[1,3,1],[1,5,1],[4,2,1]]
# mn = s.minPath(nums)

s1 = Solution1()
mn,v= s1.minSumPath(nums)
print(mn,v)