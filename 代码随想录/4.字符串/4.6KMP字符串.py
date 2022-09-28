"""
在一个串中查找是否出现过另一个串

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""

# 暴力遍历
# class Solution:
#     def KMPString(self,haystack:str,needle:str):
#         h = len(haystack)
#         n = len(needle)
#         for i in range(h-n):
#              if(haystack[i:i+n] == needle):
#                 return i
#         return -1



# kmp 算法
class Solution:
    def KMPString(self,haystack:str,needle:str):
        #
        # def getNext(needle,x):
        #     # 从x枚举到1
        #     for i in range(x,0,-1):
        #         if needle[0:i] == needle[x-i+1:x+1]:
        #             return i
        #     return 0
        def getNext(needle):
            next = []
            next.append(0) # next[0] = 0 第一个必然是0
            now = 0
            x = 1 # 从next[1]开始
            while x < len(needle):
                if needle[x] == needle[now]:
                    x += 1
                    now += 1
                    next.append(now)
                elif now:
                    now = next[now-1]
                else:
                    next.append(0)
                    x += 1
            return next
        next = getNext(needle)
        tar = 0
        pos = 0

        while(tar<len(haystack)):
            if haystack[tar] == needle[pos]:
                tar += 1
                pos += 1
            elif(pos>0):
                pos = next[pos]
                # pos = getNext(needle,pos-1) # pos = getnexts说明了 前面已经匹配过了，不需要匹配，主要是还是对模式串的历史信息进行记录
            else:
                tar += 1
            if pos == len(needle):
                ans = tar - pos
                return ans
        return -1

haystack = 'aabaacaabaaf '# "hello"
needle = 'aabaaf' # "ll"
s_ = Solution()
print(s_.KMPString(haystack,needle))
