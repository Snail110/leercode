"""
给定两个字符串text1，和text2，返回这两个字符串的最长公共子序列的长度
不连续的子序列
思路：
要求最长公共子序列，依赖于前一个公共子序列，用动态规划
1.init
dp[i][j]表示以i和j结尾的子字符串 最长公共子序列长度
2.递推公式
dp[i][j] 依赖前一个递归公式
if nums[i]==nums[j]:
dp[i][j] = dp[i-1][j-1] + 1
else:
如果没有没有相等，那么需要继承前面最长的公共子序列长度，因此需要max前面两个的最长公共子序列
dp[i][j] = max(dp[i-1][j],dp[i][j-1])
3.初始化
dp[0][0] = 0
4.遍历顺序
从左往右遍历
"""
class Solution:
    def max_len_sub_list(self,text1:str,text2:str):
        """

        :param text1:
        :param text2:
        :return:
        """
        t1 = len(text1)
        t2 = len(text2)
        dp = [[0 for _ in range(t2)] for _ in range(t1)]

        for i in range(t1):
            for j in range(t2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

text1 = '12345'
text2 = '341'

s = Solution()
print(s.max_len_sub_list(text1,text2))