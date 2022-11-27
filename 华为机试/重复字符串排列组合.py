"""
有重复字符串的排列组合，编写一种方法，计算某字符串的所有排列组合。

1、回溯方法：
排列组合+ 去重复

"""

class Solution:
    def helper(self,nums:list,res:list,path:list,used:list):
        """
        对于不重复的全排列和重复的全排列，需要考虑
        :param nums:
        :param i:
        :param res:
        :param path:
        :return:
        """
        # 终止条件
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            # 如果前一个i没用过，并且nums[i] = nums[i-1],used[i-1]==0表示同层去重复，used[i-1]==1表示同树枝去重复
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                continue
            if used[i] == 0:
                used[i] = 1
                path.append(nums[i])
                self.helper(nums,res,path,used)
                used[i] = 0
                path.pop()
        return res

    def main(self,nums:list):

        res = []
        path = []
        used = [0] * len(nums)
        nums_s = sorted(nums)
        res = self.helper(nums_s,res,path,used)
        return res

s = Solution()
nums = ['a','b','a']
print(s.main(nums))
