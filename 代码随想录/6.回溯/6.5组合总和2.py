"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明： 所有数字（包括目标数）都是正整数。 解集不能包含重复的组合。

示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]

示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]]
"""


class Solution:
    def backTrack(self,candidates:list,target:int,result:list,path:list,num_sum:int,startindex:int,used:list):
        """
        回溯
        :param candidates:
        :param target:
        :param result:
        :param path:
        :param num_sum:
        :param startindex:
        :param usered:
        :return: result
        """
        # 终止条件
        if target == num_sum:
            result.append(path[:])
            return
        if target < num_sum:
            return
        for i in range(startindex,len(candidates)):
            # 判断是否用过 used[i-1]=False 代表 同层
            if (i > 0) and (candidates[i-1] == candidates[i]) and (used[i-1] == False):
                return
            used[i] = True #记录用过
            path.append(candidates[i]) # 保存路径
            num_sum += candidates[i] # 加和
            self.backTrack(candidates,target,result,path,num_sum,i+1,used)
            used[i] = False
            path.pop()
            num_sum -= candidates[i]

    def main(self,candidates:list,target:int):
        result = []
        path = []
        used = [False] * len(candidates)
        self.backTrack(candidates,target,result,path,0,0,used)
        return result



candidates = [10,1,2,7,6,1,5]; target = 8
candidates_sort = sorted(candidates)
s = Solution()
print(s.main(candidates_sort,target))