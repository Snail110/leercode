"""
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1： 输入：nums = [1,3,5,4,7] 输出：3 解释：最长连续递增序列是 [1,3,5], 长度为3。 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。

示例 2： 输入：nums = [2,2,2,2,2] 输出：1 解释：最长连续递增序列是 [2], 长度为1。

提示：

0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
#

1、dp[i]表示以i为结尾的连续递增子序列的最大长度

2、递归函数
因为是连续递增因此只需要选择i与i+1之间的关系即可，强依赖于前面一位
if nums[i+1] > nums[i]:dp[i+1] = dp[i]+1
3、初始化
每个一开始长度都是1，因此
dp[i] = 1

"""
class Solution:
    def max_len_up_sub_list(self,nums:list):
        """"""
        # init dp dp[0] = 1
        n = len(nums)
        dp = [1] * n
        res = 0
        # 递推公式 if nums[i] > nums[i-1] : dp[i] = d[i-1] + 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                res = max(res,dp[i])
        return res
s = Solution()
nums = [1,3,5,4,7]
print(s.max_len_up_sub_list(nums))
