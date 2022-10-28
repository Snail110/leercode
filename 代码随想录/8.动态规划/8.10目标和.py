"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5

解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
#思路

本题要如何使表达式结果为target，

既然为target，那么就一定有 left组合 - right组合 = target。

left + right等于sum，而sum是固定的。

公式来了， left - (sum - left) = target -> left = (target + sum)/2 。

target是固定的，sum是固定的，left就可以求出来。

此时问题就是在集合nums中找出和为left的组合

如何转化为01背包问题呢。

假设加法的总和为x，那么减法对应的总和就是sum - x。

所以我们要求的是 x - (sum - x) = S

x = (S + sum) / 2

此时问题就转化为，装满容量为x背包，有几种方法。

大家看到(S + sum) / 2 应该担心计算的过程中向下取整有没有影响。

这么担心就对了，例如sum 是5，S是2的话其实就是无解的，所以
同时如果 S的绝对值已经大于sum，那么也是没有方案的。

本题则是装满有几种方法。其实这就是一个组合问题了。

确定dp数组以及下标的含义
dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法
确定递推公式
有哪些来源可以推出dp[j]呢？

不考虑nums[i]的情况下，填满容量为j的背包，有dp[j]种方法。

那么考虑nums[i]的话（只要搞到nums[i]），凑成dp[j]就有dp[j - nums[i]] 种方法。

例如：dp[j]，j 为5，

已经有一个1（nums[i]） 的话，有 dp[4]种方法 凑成 dp[5]。
已经有一个2（nums[i]） 的话，有 dp[3]种方法 凑成 dp[5]。
已经有一个3（nums[i]） 的话，有 dp[2]中方法 凑成 dp[5]
已经有一个4（nums[i]） 的话，有 dp[1]中方法 凑成 dp[5]
已经有一个5 （nums[i]）的话，有 dp[0]中方法 凑成 dp[5]
那么凑整dp[5]有多少方法呢，也就是把 所有的 dp[j - nums[i]] 累加起来
dp[j] += dp[j - nums[i]]

dp数组如何初始化
dp[0] = 1，理论上也很好解释，装满容量为0的背包，有1种方法，就是装0件物品。
确定遍历顺序
我们讲过对于01背包问题一维dp的遍历，nums放在外循环，target在内循环，且内循环倒序。


"""

class Solution:
    def findTargetSumWays(self,nums:list,S:int):

        if (sum(nums) + S) % 2 == 1:
            return False
        if sum(nums) < S :
            return False

        left = int((sum(nums) + S) / 2)

        # 初始 dp定义
        dp = [0] * (left + 1)
        dp[0] = 1

        # 递推公式 dp[j] += dp[j-nums[i]]
        # 遍历
        for i in range(len(nums)):
            for j in range(left, nums[i] - 1, -1):
                dp[j] += dp[j-nums[i]]

        return dp[left]


s = Solution()
nums = [1, 1, 1, 1, 1]; S = 3
print(s.findTargetSumWays(nums,S))

