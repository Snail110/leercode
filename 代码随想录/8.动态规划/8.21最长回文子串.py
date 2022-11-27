"""
最长回文子序列
力扣题目链接(opens new window)

给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1: 输入: "bbbab" 输出: 4 一个可能的最长回文子序列为 "bbbb"。

示例 2: 输入:"cbbd" 输出: 2 一个可能的最长回文子序列为 "bb"。

提示：

1 <= s.length <= 1000
s 只包含小写英文字母
#思路
1.define
dp[i][j]:在区间i，j之间的最长的回文子串序列
2.递推公式
从中心开花，然后往两边延展，这样
dp[i][j]依赖于dp[i+1][j-1]
如果dp[i]=dp[j]，那么dp[i][j] = dp[i+1]dp[j-1] + 2
如果dp[i] ！= dp[j],那么 dp主要依赖dp[i][j-1] 或者依赖于 dp[i+1][j]
dp[i][j] = max(dp[i][j-1],dp[i+1][j])
3.init
当i=j时，dp[i][i] = 1,单个字符也是回文子序列，为1，其他的为0
4.遍历顺序
因为从递推公式来看，dp[i][j]依赖于dp[i+1][j-1]，那么对于i来说 遍历从高到滴，j从低到高

"""

class Solution:
    def max_len_huiwen(self,huiwen:str):

        len_ = len(huiwen)
        # define dp[i][j]
        # 初始化
        dp = [[0 for _ in range(len_)] for _ in range(len_)]

        for i in range(len_):
            dp[i][i] = 1

        for i in range(len_-2,-1,-1):
            for j in range(i+1,len_):
                if huiwen[i] == huiwen[j]:
                    dp[i][j] = max(dp[i][j],dp[i+1][j-1] + 2)
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])

        return dp[0][len_-1]

s = Solution()
huiwen = 'bbbbb'
print(s.max_len_huiwen(huiwen))
