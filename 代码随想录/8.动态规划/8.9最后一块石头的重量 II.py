"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎； 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
求石头最小剩下多少？
示例： 输入：[2,7,4,1,8,1] 输出：1 解释： 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]， 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]， 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]， 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

本题其实就是尽量让石头分成重量相同的两堆，相撞之后剩下的石头最小，这样就化解成01背包问题了

接下来进行动规五步曲：

确定dp数组以及下标的含义
dp[j]表示容量（这里说容量更形象，其实就是重量）为j的背包，最多可以背dp[j]这么重的石头。

确定递推公式
01背包的递推公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

本题则是：dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);

一些同学可能看到这dp[j - stones[i]] + stones[i]中 又有- stones[i] 又有+stones[i]，看着有点晕乎。

还是要牢记dp[j]的含义，要知道dp[j - stones[i]]为 容量为j - stones[i]的背包最大所背重量。

dp数组如何初始化
既然 dp[j]中的j表示容量，那么最大容量（重量）是多少呢，就是所有石头的重量和。

因为提示中给出1 <= stones.length <= 30，1 <= stones[i] <= 1000，所以最大重量就是30 * 1000 。

而我们要求的target其实只是最大重量的一半，所以dp数组开到15000大小就可以了。

当然也可以把石头遍历一遍，计算出石头总重量 然后除2，得到dp数组的大小。

我这里就直接用15000了。

接下来就是如何初始化dp[j]呢，因为重量都不会是负数，所以dp[j]都初始化为0就可以了，这样在递归公式dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);中dp[j]才不会初始值所覆盖。
确定遍历顺序
如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒序遍历！

举例推导dp数组

"""

class Solution:
    def minWeightStone(self,nums:list):
        """
        dp
        :param nums:
        :return:
        """
        # 初始化以及定义：dp[j] 表示容量为j时，背包最大重量
        dp = [0 for i in range( int(30 * 1000 / 2) + 1)]
        # 递推公式 weight[i] = nums[i] value[i] = nums[i] dp[j] = max(dp[j], dp[j-weight[i]]) + value[i]) =  max(dp[j], dp[j-nums[i]]) + nums[i])
        # 遍历顺序一维dp
        target = int(sum(nums) / 2) # 目标值
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])

        return sum(nums) - dp[target] - dp[target]



s = Solution()
nums = [2,7,4,1,8,1]
print(s.minWeightStone(nums))

