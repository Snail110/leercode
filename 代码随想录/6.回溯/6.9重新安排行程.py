"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

提示：

如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次。
示例 1：

输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2：

输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后\

"""

from collections import defaultdict
class Solution:
    def main(self,nums:list):
        """
        回溯 不重复
        :param nums:
        :param result:
        :return:
        """
        # 单层逻辑
        ticker = defaultdict(list) # {key:[value1,value2]}
        for i in nums:
            ticker[i[0]].append(i[1])
        result =[]
        result.append("JFK")
        def backtrack(start_point):
            # 终止条件
            if len(result) == len(nums) + 1:
                return True
            ticker[start_point].sort()
            # ticker = ['JKL':{"SFO','ATL'}]
            for i in ticker[start_point]:
                end_point = ticker[start_point].pop(0)
                result.append(end_point)
                if backtrack(end_point):
                    return True
                result.pop()
                ticker[start_point].append(end_point)
        backtrack("JFK")
        return result


nums = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s = Solution()
print(s.main(nums))


