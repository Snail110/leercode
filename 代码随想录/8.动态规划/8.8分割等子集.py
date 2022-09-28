"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200

示例 1: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2: 输入: [1, 2, 3, 5] 输出: false 解释: 数组不能分割成两个元素和相等的子集.

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
#思路
1.判断是否可以用dp
2.如果可以用，转化为dp形式
3.按照dp流程确定每一步
4.书写代码

首先该题可以转化为是否可以选出子集和满足sum/2,如果满足那么该题目成立，并且每次元素只能用一次，这是01背包问题
确定01背包问题的流程
1.dp定义以及初始化
dp[j]代表背包重量为j，最大价值为dp[j]，价值value[i]可以为nums[i],weight[i]也可以表示为nums[i]
因为都为正整数因此，初始值为：dp[i] = 0
2.dp递归公式
采用常规的01背包递归函数，dp[j] = max(dp[j],dp[j-weight[i]] + value[i]) = max(dp[j],dp[j-nums[i]] + nums[i])
3.遍历顺序
遍历元素，再倒序遍历背包重量，重量从大到小遍历


"""
class Solution:
    def splitSameSum(self,nums:list):
        """

        :param nums:
        :return:
        """
        # 初始化dp
        cols = int(100 * 200 / 2)
        rows = len(nums)
        if sum(nums) % 2 == 1:
            return False
        target = int(sum(nums) / 2)
        dp = [0 for _ in range(cols)]   # j为累计和
        # rows代表物品个数 cols代表重量 重量范围为0-int(100 * 200 / 2)
        for i in range(rows):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]] + nums[i])

        res = True if dp[target] == target else False
        return res


s = Solution()
nums = [1, 2, 2, 5]
print(s.splitSameSum(nums))


