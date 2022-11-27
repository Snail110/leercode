"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1： 输入：nums = [10,9,2,5,3,7,101,18] 输出：4 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2： 输入：nums = [0,1,0,3,2,3] 输出：4

示例 3： 输入：nums = [7,7,7,7,7,7,7] 输出：1

提示：

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 104
#

dp[i]的定义
dp[i]表示i之前包括i的以nums[i]结尾最长上升子序列的长度

状态转移方程
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。

所以：if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);

注意这里不是要dp[i] 与 dp[j] + 1进行比较，而是我们要取dp[j] + 1的最大值。

dp[i]的初始化
每一个i，对应的dp[i]（即最长上升子序列）起始大小至少都是1.

确定遍历顺序
dp[i] 是有0到i-1各个位置的最长升序子序列 推导而来，那么遍历i一定是从前向后遍历。

j其实就是0到i-1，遍历i的循环在外层，遍历j则在内层，代码如下

1、# init
dp[i] 表示 i之前包括i的以nums[i] **结尾** 的最长递增子序列长度

注意结尾的 这样的定义 只能求出来当前结尾的最大，并不能求出来全部的最大，因此必须res变量记录当前的最大
2、状态方程
if nums[i] > nums[j]:dp[i] = max(dp[i],dp[j]+1) j = 从0到i-1
"""

class Solution:
    def max_len_nums(self,nums:list):
        """

        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return len(nums)
        # init
        len_ = len(nums)
        dp = [1] * (len_+1)
        res = 0
        for i in range(1,len_):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                if dp[i] > res:
                    res = dp[i]
        return dp

nums = [0,1,3,4,5,6]

s = Solution()
print(s.max_len_nums(nums))
