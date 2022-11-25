"""
05 将字符串s中的每个空格替换成'%20'
例如：
s = 'we are happy'
output = 'we%20are%20happy'
"""

class Solution:
    def replace_s(self,s:str):
        """

        :param s:
        :param rep:
        :return:
        """
        left = len(s)

        for i in s:
            if i == ' ':
                s += '00'
        s_list = list(s)
        right = len(s_list)
        for i in range(left-1,-1,-1):
            if s_list[i] == ' ':
                s_list[right-3:right] = list('%20')
                right -= 3
            else:
                s_list[right-1] = s_list[i]
                right -= 1

        return s_list

k = 'we are happy'
s = Solution()
print(s.replace_s(k))

