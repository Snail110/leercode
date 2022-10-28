"""
以数组nums表示若干个区间的集合，其中单个区间为nums[i] =[start_i,end_i]，
合并所有重叠的区间，并且返回一个不重叠的区间数组，该数组恰好覆盖输入中的所有区间

nums = [[1,3],[2,6],[8,10],[12,18]]
输出为
[[1,6],[8,10],[12,18]]
"""
import sys

# class Solution:
#     def main(self,nums:list):
#         """
#
#         :param nums:
#         :return:
#         """
#         nums_s = sorted(nums,key = lambda x:(x[0]))
#         print(nums_s)
#         res = []
#         left = nums_s[0][0]
#         right = nums_s[0][1]
#
#         for i in range(len(nums_s)):
#             if right >= nums_s[i][0]:
#                 right = max(nums_s[i][1],right)
#             else:
#                 res.append([left,right])
#                 left = nums_s[i][0]
#                 right = nums_s[i][1]
#         res.append([left,right])
#         return res

class Solution:
    def main(self,nums:list):
        """

        :param nums:
        :return:
        """
        nums_s = sorted(nums, key=lambda x: (x[0]))
        res = []
        for i in nums_s:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])

        return res
nums = [[1,3],[2,6],[4,10],[12,18],[20,21]]
s = Solution()
print(s.main(nums))