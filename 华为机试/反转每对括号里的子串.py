"""
出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

 

示例 1：

输入：s = "(abcd)"
输出："dcba"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
反转 字符串要么用递归要么用栈模拟
本题用栈
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        用栈
        :param s:
        :return:
        """
        stack = [] # 栈 先进后出

        for i in s:
            if i !=')':
                # 非右括号，一直塞进去
                stack.append(i)
            else:
                # 如果等于),那么将原来的元素弹出来
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                # 弹出来 (
                if stack:
                    stack.pop()
                # 将反转好的字串 重新塞进去
                stack += tmp

        return ''.join(stack)


class Solution2:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        pair = [0] * n

        # 预先存储左右括号的映射关系
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        index = 0
        # step = 1 表示向右走, step = -1 表示向左走
        step = 1
        result = []
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = pair[index]
                # 走的方向反转
                step = -step
            else:
                result.append(s[index])
            index += step
        return "".join(result)

l = '(a(bc)d)'
s = Solution()
print(s.reverseParentheses(l))