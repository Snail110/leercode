"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."
"""

class Solution:
    def replaceSpace(self,s:str,replace_s='%20'):
        s_list = list(s)
        count = s.count(" ") # 统计空格数
        s_list.extend([","] * count*2) # 增加空格数，满足增添后的长度
        left = len(s)-1
        right = len(s_list)-1
        while(left>=0):
            if s_list[left] != ' ':
                s_list[right] = s_list[left]
                right -= 1
            else:
                s_list[right] = '0'
                s_list[right-1] = '2'
                s_list[right-2] = '%'
                right -= 3
            left -= 1

        return ''.join(s_list)

s = "We are happy."
s_ = Solution()
print(s_.replaceSpace(s))
