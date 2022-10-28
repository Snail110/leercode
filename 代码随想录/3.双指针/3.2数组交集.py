"""
题意：给定两个数组，编写一个函数来计算它们的交集。
"""

class Solution:
    def isAngram(self,s:list,t:list):
        return list(set(s) & set(t))

s = [1,2,2,33]
t = [1,2]
isAngram = Solution()
print(isAngram.isAngram(s,t))

