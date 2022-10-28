"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况

子序列不允许改变 原序列，因此不能排序
"""
class Solution:
    def backtrack(self,nums:list,path:list,result:list,startindex:int):
        """
        子序列 递增，回溯，去重
        :param nums:
        :param path:
        :param result:
        :param startindex:
        :return: result
        """
        # 子增2个
        if len(path) > 1:
            result.append(path[:])
        if startindex > len(nums):
            return
        # 单层逻辑
        used = set()
        for i in range(startindex,len(nums)):
            # 判断 子增，重复
            if (len(path)>1 and path[-1] > nums[i] or nums[i] in used):
                continue
            used.add(nums[i])
            path.append(nums[i])
            self.backtrack(nums,path,result,i+1)
            path.pop()

    def main_(self,nums:list):
        path = []
        result = []
        startinedx = 0
        self.backtrack(nums,path,result,startinedx)
        return result

nums = [4, 6, 7, 7]
s = Solution()
print(s.main_(nums))