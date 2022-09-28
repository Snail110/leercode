"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]

去重复
"""

class Solution:
    def backtracking(self,num:list,result:list,path:list,startindex:int,used:list):
        """
         排序 回溯 去重复
        :param num:
        :param result:
        :param path:
        :param startindex:
        :param used:
        :return:
        """
        # 终止条件
        result.append(path[:])
        if startindex > len(num):
            return
        # 单层逻辑
        for i in range(startindex,len(num)):
            # 去重复逻辑
            if i > 0 and num[i-1] == num[i] and used[i-1] == False:
                return
            path.append(num[i])
            used[i] = True # 递归时， 赋值True
            self.backtracking(num,result,path,i+1,used)
            path.pop()
            used[i] = False


    def main(self,num:list):
        result = []
        path = []
        startindex = 0
        used = [False] * len(num)
        self.backtracking(num,result,path,startindex,used)
        return result

num = [1,2,2]
s = Solution()
num_s = sorted(num)
print(s.main(num_s))
