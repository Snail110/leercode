"""
给定一个字符串，寻找无重复的最长字符串
滑动窗口：维护一个窗口队列，不断地去扩大右边边界，如果出现重复的字符，那么一直弹出左边的字符，直到无重复为止，此时为最长
"""

class Solution:
    def max_len_substring(self,s:str):
        """

        :param s:
        :return:
        """
        vec = [] # 保存滑动窗口队列
        res = 0 # 最大长度
        for i in range(len(s)):
            while vec and s[i] in vec:
                vec.pop(0)
            vec.append(s[i])
            res = max(res,len(vec))

        return res

s = Solution()
string = 'abcabcbb'
print(s.max_len_substring(string))
