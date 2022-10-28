"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]

"""

class Solution:
    def backtracking(self, k:int, n:int, startindex:int, sum_i :int, path:list, result:list):
        """
        回溯
        :param k:
        :param n:
        :param path:
        :param result:
        :return:
        """
        # 终止条件 path len = k
        if len(path) == k:
            if sum_i == n:
                result.append(path[:])
            return

        # 单层逻辑 宽度 1-9 深度 k
        for i in range(startindex,10):
            path.append(i) #节点处理
            sum_i += i #节点处理
            self.backtracking(k, n, i+1, sum_i, path, result) # 递归 i+1
            path.pop() # 回溯
            sum_i -= i # 回溯

    def sumList(self,k:int,n:int):
        path = []
        result = []
        startindex = 1
        sum_i = 0
        self.backtracking(k, n, startindex, sum_i, path, result)
        return result

k = 3; n = 9
s = Solution()
print(s.sumList(k, n))