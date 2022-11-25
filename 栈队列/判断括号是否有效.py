"""
判断式子是否有效括号
s = '()[]{}' true
s = '{]' false
解法：
括号匹配是使用栈解决的经典问题
"""
class Solution:
    def is_valid(self,s:list):
        """

        :param s:
        :return:
        """
        stack = []
        d_str = {')':'(',']':'[','}':'{'}
        for i in s:
            # 如果在右括号
            if i in ['(','[','{']:
                stack.append(i)
            elif stack and stack[-1] == d_str[i]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True

s = Solution()
t = '((([{}])'
print(s.is_valid(t))
