"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母
"""

# class Solution:
#     def isAngram(self,s:str,t:str):
#         array_ = [0] * 26
#         for i in range(len(s)):
#             array_[ord(s[i])-ord('a')] += 1
#
#         for j in range(len(t)):
#             array_[ord(t[j])-ord('a')] -= 1
#
#         for k in array_:
#             if k !=0:
#                 return False
#         return True

class Solution:
    def isAngram(self,s:str,t:str):
        dict1_= dict()
        dict2_= dict()
        for i in s:
            if i not in dict1_:
                dict1_[i] = 1
            else:
                dict1_[i] += 1

        for j in t:
            if j not in dict2_:
                dict2_[j] = 1
            else:
                dict2_[j] += 1
        return dict1_ == dict2_

s = "anagram"
t = "nagaram"
isAngram = Solution()
print(isAngram.isAngram(s,t))
