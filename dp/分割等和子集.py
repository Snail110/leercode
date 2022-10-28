"""
题目难易：中等

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200

示例 1: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2: 输入: [1, 2, 3, 5] 输出: false 解释: 数组不能分割成两个元素和相等的子集.

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100

转化背包问题：
分为两个等和sum/2的 区间,分割为2个子集，只要其中区间的和为sum/2就可以

dp[j] 表示背包提及为j的，最大能凑成和为j的子集
这里不关心最大，只关心dp[sum/2]是否存在，如果存在那么就有答。
"""

class Solution:
    def sub_sum(self,nums:list):
        """

        :param nums:
        :return:
        """
        # init
        if sum(nums) % 2 != 0:
                return False
        sum2_ = int(sum(nums) / 2)
        dp = [0] * (sum2_+1)

        # 遍历 先物品后背包 倒序，并且遍历到nums[i]停止
        for i in range(len(nums)):
            for j in range(sum2_,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]] + nums[i])

        return dp[sum2_] == sum2_

nums = [1, 5, 10]
s = Solution()
print(s.sub_sum(nums))
