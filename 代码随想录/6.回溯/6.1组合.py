"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]

"""

# class Solution:
#     def conbine(self,n:int,k:int):
#         path = []
#         result = []
#         startindex = 1
#         def backtracking( n: int, k: int, startindex: int):
#             """
#             回溯
#             :param n:
#             :param k:
#             :param startindex:
#             :return: result, path
#             """
#             # 终止条件
#             if (len(path) == k):
#                 # 保存path 无饭返回值
#                 result.append(path[:])
#                 return
#             # 回溯逻辑 注意是n+1
#             for i in range(startindex, n + 1):
#                 # 节点处理
#                 path.append(i)
#                 backtracking(n, k, i + 1)
#                 path.pop()
#             return
#
#         backtracking(n, k, startindex)
#         return result


class Solution:
    def backtracking(self,n: int, k: int, startindex: int,path:list,result:list):
        """
        回溯
        :param n:
        :param k:
        :param startindex:
        :return: result, path
        """
        # 终止条件
        if (len(path) == k):
            # 保存path 无饭返回值
            result.append(path[:]) # 注意这里必须为深拷贝 不能哥白尼path公共用 地址
            return
        # 回溯逻辑 注意是n+1
        for i in range(startindex, n + 1):
            # 节点处理
            path.append(i)
            self.backtracking(n, k, i + 1,path,result)
            path.pop()
        return
    def conbine(self,n:int,k:int):
        path = []
        result = []
        startindex = 1

        self.backtracking(n, k, startindex,path,result)
        return result

n = 4
k = 2
s = Solution()
print(s.conbine(n, k))


