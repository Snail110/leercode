"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成
解题思路：
数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，也就是一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。
"""
class Solution:
    def isAgainString(self,s:str):

        def getNext(s:str):
            next = []
            x = 1 # 从next[1]开始
            now = 0
            next.append(0)

            while x<len(s):
                if s[now] == s[x]:
                    now += 1
                    x += 1
                    next.append(now)
                elif now:
                    now = next[now-1] # 向前缩短寻找相同的字符串
                else:
                    next.append(0)
                    x += 1
            return next

        next = getNext(s) # next 数组
        print(next)
        sLen = len(s)
        maxLen = next[-1]
        if next[-1] != 0 and sLen % (sLen - maxLen) == 0:
            return True
        else:
            return False

s = Solution()
p = 'a'
print(s.isAgainString(p))


