"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]

注意[]也是一种情况，记录树所有节点，终止条件 剩余集合没有了，都取完了

子集是收集树形结构中树的所有节点的结果。而组合问题、分割问题是收集树形结构中叶子节点的结果
"""

class Solution:
    def backtracking(self,nums:list,result:list,path:list,startindex:int):
        """
        回溯，保存树所有节点
        :param nums:
        :param result:
        :param path:
        :param startindex:
        :return: result
        """
        # 放在外面，每次都要保存节点  收集子集，要先于终止判断
        result.append(path[:])

        # 终止条件
        if startindex > len(nums):
            return

        # 单层逻辑
        for i in range(startindex,len(nums)):
            # 节点处理
            path.append(nums[i])
            self.backtracking(nums,result,path,i+1)
            path.pop()


    def main(self,nums:list):
        result = []
        path = []
        startidex = 0
        self.backtracking(nums,result,path,startidex)
        return  result

nums = [1,2,3]
s = Solution()
print(s.main(nums))

