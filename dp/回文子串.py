"""
leetcode：647
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc" 输出：3 解释：三个回文子串: "a", "b", "c"

示例 2：

输入："aaa" 输出：6 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：

输入的字符串长度不会超过 1000 。


根据回文子串的定义：回文串”是一个正读和反读都一样的字符串，也就是关于中心对称的字符串
那么从中心往两边进行延展，相等就是回文串
两种方法：
双指针法：
1、遍历每个字符，从每个字符开始往两边延展，
这里分2种情况，1种是从一个字符开始，1种是从两个字符开始

dp方法：
1、define
dp[i][j]: 代表为i和j的字符串是否是回文，为布尔类型
2、递推公式
dp[i][j]：
根据回文串定义 if s[i] = s[j]：
如果i=j，那么确实是回文，例如a dp[i][j] = True，res += 1
如果i = j-1，那么也是，例如aa，dp[i][j] = True，res += 1
如果j-i >=2，这种情况需要考虑 除了i和j以外的子串是否是会文，例如cbc，caac，cabac。
if dp[i+1][j-1]:
dp[i][j] = True,res += 1

3、遍历顺序：
从递推公式来看：
i从下往上，j从左往右遍历
"""
# class Solution:
#     def main(self,s:str):
#         """
#
#         :param s:
#         :return:
#         """
#         def extend(s,i,j,n):
#             res = 0
#             while i >=0 and j < n and s[i]==s[j]:
#                 res += 1
#                 i -= 1
#                 j += 1
#             return res
#         result = 0
#         for i in range(len(s)):
#             result += extend(s,i,i,len(s))
#             result += extend(s,i,i+1,len(s))
#         return result

# a = 'aaa'
# s = Solution()
# s.main(a)

class Solution2:
    def main(self,s:str):
        """

        :param s:
        :return:
        """
        # define init
        len_ = len(s)
        dp = [[False for _ in range(len_)] for _ in range(len_)]
        for i in range(len_):
            dp[i][i] = True

        res = 0
        for i in range(len_-1,-1,-1):
            for j in range(i,len_):
                if s[i] == s[j]:
                    if j-i<=1:
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
        return res

s = Solution2()
a = 'aba'
print(s.main(a))