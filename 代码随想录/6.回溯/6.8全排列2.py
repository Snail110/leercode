"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出： [[1,1,2], [1,2,1], [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

组合问题和排列问题是在树形结构的叶子节点上收集结果，而子集问题就是取树上所有节点的结果。
"""

class Solution:
    def backtrack(self,nums:list,path:list,result:list,used:list):
        """
        重复 排序 回溯 全排列
        :param nums:
        :param path:
        :param result:
        :param used:
        :return:
        """
        # 终止条件
        if len(path) == len(nums):
            result.append(path[:])
            return

        # 处理单层逻辑
        for i in range(len(nums)):
            # 处理重复元素 相邻相等 并且 used[i-1]=False代表同层用过了，
            # // used[i - 1] == true，说明同一树枝nums[i - 1]使用过
            # // used[i - 1] == false，说明同一树层nums[i - 1]使用过
            # // 如果同一树层nums[i - 1]使用过则直接跳过
            if (i > 0 and nums[i] == nums[i-1] and used[i-1] == False):
                continue
            if used[i] == False:
                path.append(nums[i])
                used[i] = True
                self.backtrack(nums,path,result,used)
                path.pop()
                used[i] = False


    def main(self,nums:list):
        path = []
        result = []
        used = [False] * len(nums)
        self.backtrack(nums,path,result,used)
        return result

nums = [1,2,3]
nums_s = sorted(nums)
s = Solution()
print(s.main(nums_s))
