"""
爬楼梯
力扣题目链接(opens new window)

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1： 输入： 2 输出： 2 解释： 有两种方法可以爬到楼顶。

1 阶 + 1 阶
2 阶
示例 2： 输入： 3 输出： 3 解释： 有三种方法可以爬到楼顶。

1 阶 + 1 阶 + 1 阶
1 阶 + 2 阶
2 阶 + 1 阶

改为：一步一个台阶，两个台阶，三个台阶，.......，直到 m个台阶。问有多少种不同的方法可以爬到楼顶呢？

1阶，2阶，.... m阶就是物品，楼顶就是背包。

每一阶可以重复使用，例如跳了1阶，还可以继续跳1阶。

问跳到楼顶有几种方法其实就是问装满背包有几种方法。

此时大家应该发现这就是一个完全背包问题了！

在动态规划：494.目标和 (opens new window)、 动态规划：518.零钱兑换II (opens new window)、动态规划：377.
 组合总和 Ⅳ (opens new window)中我们都讲过了，求装满背包有几种方法，递推公式一般都是dp[i] += dp[i - nums[j]];

本题呢，dp[i]有几种来源，dp[i - 1]，dp[i - 2]，dp[i - 3] 等等，即：dp[i - j]

那么递推公式为：dp[i] += dp[i - j]
"""

class Solution:
    def climbStairs(self,n:int,m:int):
        """
        完全背包 排列问题 先背包重量，再物品排列
        :param n:
        :param m:
        :return:
        """
        # 初始化定义 dp[i]表示i个台阶，有几种排列方式
        dp = [0] * (n + 1)
        dp[0] = 1
        # 递推公示 dp[i] += dp[i-j] i为台阶数，j为步数
        for i in range(n+1):
            for j in range(m):
                if i - j >= 0:
                    dp[i] += dp[i-j]

        return dp[n]

s = Solution()
n = 3
m = 3

print(s.climbStairs(n,m))