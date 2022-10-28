"""
给定taget和nums，找出和大于等于target的最小长度
例如nums = [2，3，1，2，4，3】 target=7
2 = [4,3]
滑动窗口：
"""

class Solution:
    def min_len_nums(self,nums:list,target:int):
        """

        :param nums:
        :param target:
        :return:
        """
        i = 0
        min_len = len(nums)
        len_ = len(nums)
        sum_ = 0
        for j in range(len_):
            sum_ += nums[j]
            while sum_ >= target:
                min_len = min(min_len, j-i+1)
                sum_ -= nums[i] # 滑动窗口的精髓
                i += 1

        return min_len


nums = [2,3,1,2,4,3,1];target=7
s = Solution()
print(s.min_len_nums(nums,target))
