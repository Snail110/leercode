"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例: 输入: [-2,1,-3,4,-1,2,1,-5,4] 输出: 6 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6

贪心贪的是哪里呢？

\如果 -2 1 在一起，计算起点的时候，一定是从1开始计算，因为负数只会拉低总和，这就是贪心贪的地方！

局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。

全局最优：选取最大“连续和”

局部最优的情况下，并记录最大的“连续和”，可以推出全局最优

从代码角度上来讲：遍历nums，从头开始用count累积，如果count一旦加上nums[i]变为负数，

那么就应该从nums[i+1]开始从0累积count了，因为已经变为负数的count，只会拖累总和。

这相当于是暴力解法中的不断调整最大子序和区间的起始位置。

那有同学问了，区间终止位置不用调整么？ 如何才能得到最大“连续和”呢？

区间的终止位置，其实就是如果count取到最大值了，及时记录下来了。例如如下代码

"""

import sys
class Solution:
    def maxSumSubList(self,nums:list):
        count = 0 # 计数器
        result = - 2 ** 64 - 1# 存放结果
        for i in range(len(nums)):
            count = count + nums[i]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSumSubList(nums))
