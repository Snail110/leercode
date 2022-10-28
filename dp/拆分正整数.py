"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58
"""

class Solution:
    def max_value(self,n:int):
        """

        :param n:
        :return:
        """
        # 定义dp 返回dp[n]
        dp = [0] * (n+1)
        # 初始化
        dp[2] = 1

        # fx
        for i in range(3,n+1):
            for j in range(1,i):
                # 因为求最大值，dp[i]在内层循环有多种值，因此需要max，(i-j) * j 代表拆分2个整数，dp[i-j] * j代表拆分2个以上的整数
                dp[i] = max(dp[i],(i-j) * j,dp[i-j] * j)

        return dp

s = Solution()
print(s.max_value(10))
