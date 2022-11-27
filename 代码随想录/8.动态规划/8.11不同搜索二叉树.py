"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""

class Solution:
    def tree_nums(self,n:int):
        """

        :param n:
        :return:
        """

        # define init dp[i]表示从1到n节点组成的搜索二叉树数量
        dp = [0] * (n+1)
        # 空节点也代表一种搜索二叉树
        dp[0] = 1

        for i in range(1,n+1):
            for j in range(0,i):
                dp[i] += dp[j] * dp[i-1-j]

        return dp

s = Solution()
print(s.tree_nums(4))