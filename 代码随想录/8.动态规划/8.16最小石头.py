"""
题目难度：中等

有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎； 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

示例： 输入：[2,7,4,1,8,1] 输出：1 解释： 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]， 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]， 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]， 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000
#
转化01背包问题：
分为2个石头区间，计算其中的差值最小。
分为sum/2的区间，然后计算其最大能装多少的石头重量a，（在sum/2区间内 石头重量越大，差值越小），然后另外的区间的石头重量为sum-a,那么最小的石头为target-a-a

dp[j]表示区间体积为j的背包，最多能装多大的石头重量，其实就是遍历，只不过借用了之前的值
"""

class Solution:
    def min_stone(self,nums:list):
        """

        :param nums:
        :return:
        """

        # init
        mid_ = sum(nums) // 2
        dp = [0] * (mid_ + 1)

        for i in range(len(nums)):
            for j in range(mid_,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]] + nums[i])

        return (sum(nums) - dp[mid_]) - dp[mid_]

nums = [2,4]
s = Solution()
print(s.min_stone(nums))
