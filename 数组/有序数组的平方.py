"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]

示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]

"""
class Solution:
    def nums_pow(self,nums:list):
        """
        双指针法：有序数组，那么两边的数组平方肯定存在最大，因此left right从两边开始遍历
        :param nums:
        :return:
        """

        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        index = 0
        while left <= right:
            r = nums[right] * nums[right]
            l = nums[left] * nums[left]
            if r > l:
                ans[index] = r
                right -= 1
            else:
                ans[index] = l
                left += 1
            index += 1
        return ans

s = Solution()
nums = [-4,-1,0,3,10]
print(s.nums_pow(nums))
