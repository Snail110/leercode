"""
二维数组路径最小和，并且求的最小路径
思路：
求最小路径和，并且结果依赖于中间的结果，那么用动态规划来算
1.init
dp[i][j] 表示位置i.j的最小路径和
2.递推公式
因为最小路径和只能向右和向下走，因此dp[i][j]依赖于dp[i-1][j] dp[i]dp[j-1]
dp[i][j] = min(dp[i][j],dp[i-1][j] + nums[i][j],dp[i][j-1] + nums[i][j]
3.初始化
dp[0][0] = nums[0][0]
4.遍历顺序
从左向右，从上往下
"""

# 动态规划
class Solution:
    def min_sum_path(self,nums:list):
        """

        :param nums:
        :return:
        """
        m = len(nums)
        n = len(nums[0])
        # init
        dp = [[2 ** 32 for _ in range(n)] for _ in range(m)]
        dp[0][0] = nums[0][0]
        # 遍历
        for i in range(m):
            for j in range(n):
                dp[i][j] = min(dp[i][j],dp[i][j-1] + nums[i][j],dp[i-1][j] + nums[i][j])

        return dp

nums = [[1,3,1],[1,5,1],[4,2,1]]
s1 = Solution()
dp = s1.min_sum_path(nums)
print(dp)