"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> tru
"""

class Solution:
    def canConstruct(self,a:str,b:str):
        arr = [0] * 26 # 利用数值记录出现恶道字符串个数

        for i in b:
            arr[ord(i)-ord('a')] += 1
        for j in a:
            arr[ord(j)-ord('a')] -= 1
            if arr[ord(j)-ord('a')] < 0:
                return False
        return True

s = Solution()
a = 'ab'
b = 'acb'
print(s.canConstruct(a,b))

