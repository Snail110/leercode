"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个
"""

class Solution:
    def reverseString(self,s:str):

        # 反转字符串
        def reverseWord(s:str,left:int,right:int):
            s_list = list(s)
            while(left<right):
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left += 1
                right -= 1
            return ''.join(s_list)
        # 去除空格
        def trimHeadString(s:str):
            # 开头空格，结尾空格，中间空格
            left = 0
            right = len(s) - 1
            # 开头空格
            while(left < right and s[left] == ' '):
                left += 1
            # 结尾空格
            while(left<right and s[right] == ' '):
                right -= 1
            # 中间空格
            s_ = list(s[left:right+1])
            left = 0
            right = 0
            while(right<len(s_)):
                if (right > 0 and s_[right] == s_[right-1] and s_[right-1] == ' '):
                    right += 1
                else:
                    s_[left] = s_[right]
                    left += 1
                    right += 1
            return ''.join(s_[:left])

        # 去除空格
        s = trimHeadString(s)
        # 反转整个字符串
        s = s[::-1]
        # 反转 单词
        start = 0
        end = 0
        n = len(s)
        while(start<n):
            while end < n and s[end] != ' ':
                end += 1
            s = reverseWord(s,start,end-1)
            start = end + 1
            end += 1
        return s

s = '  hello   world  '
s_ = Solution()
print(s_.reverseString(s))

