"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况

1、输入参数 nums,path，res，startindex，
2、终止条件，不需要终止，当path大于1时，需要保存res中
3、由于不能同层用重复的数字，因此需要set记录用过的元素
"""

class Solution:
    def up_sub_list(self,nums:list,path:list,res:list,startindex:int):
        """

        :param nums:
        :param path:
        :param res:
        :param startindex:
        :return:
        """
        # 保存 path
        if len(path) > 1:
            res.append(path[:])
        used_set = set()
        for i in range(startindex,len(nums)):
            if len(path) > 1 and nums[i] < path[-1] or nums[i] in used_set:
                continue
            used_set.add(nums[i])
            path.append(nums[i])
            self.up_sub_list(nums,path,res,i+1)
            path.pop()

        return res

    def main(self,nums:list):
        path = []
        res = []
        startindex = 0
        res = self.up_sub_list(nums,path,res,startindex)
        return res


nums = [4, 6, 7, 7]
s = Solution()
print(s.main(nums))