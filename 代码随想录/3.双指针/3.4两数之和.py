"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
"""

class Solution:
    def twoNumberSum(self,nums:list,target:int):
        tmp_set = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in tmp_set:
                return [tmp_set[diff],i]
            else:
                tmp_set[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoNumberSum(nums,target))
