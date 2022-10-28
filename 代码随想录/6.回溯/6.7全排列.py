"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]

"""

class Solution:
    def backtrack(self,nums:list,path:list,result:list,used:list):
        """
        树枝重复， 回溯 有序
        :param nums:
        :param path:
        :param result:
        :param used:
        :return: result
        """
        # 终止条件
        if len(path) == len(nums):
            result.append(path[:])
            return

        # 单层逻辑
        for i in range(len(nums)):

            # 同一路径，与同一层的区别重复的不能再用
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums,path,result,used)
            used[i] = False
            path.pop()

    def main(self,nums:list):
        path  = []
        result = []
        used = [False] * len(nums)
        self.backtrack(nums,path,result,used)
        return result

nums = [1,2,3]
s = Solution()
print(s.main(nums))


