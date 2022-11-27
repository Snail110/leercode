"""
两数之和
给定一个target和nums，找出和为目标值的两个证书，并且返回数组下标，
每种输入只会对应一个答案，但是数组中同一个元素不能使用2遍

nums=[2,7,11,15],target=9
返回[0,1]
"""

class Solution:
    def tow_num_sum(self,nums:list,target:int):
        """

        :param nums:
        :param target:
        :return:
        """
        # 保存输出list
        res = []
        # 将遍历过的结果存在dict
        num_dict = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in num_dict:
                num_dict[nums[i]] = i
            else:
                res.append([num_dict[diff],i])

        return res

nums=[2,7,11,15]
target=9
s = Solution()
print(s.tow_num_sum(nums,target))