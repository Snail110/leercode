"""
递归也是用栈来实现的！！

根据 逆波兰表示法，求表达式的值。

有效的运算符包括 + ,  - ,  * ,  / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：

输入: ["2", "1", "+", "3", " * "]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

"""
class Solution:
    def main(self,nums:list):
        """

        :param nums:
        :return:
        """
        stack = []

        for i in range(len(nums)):
            if nums[i] not in ['+','-','*','/']:
                stack.append(nums[i])
            elif nums[i] == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif nums[i] == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a - b)
            elif nums[i] == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif nums[i] == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a / b)
        return stack[0]

nums = ["2", "1", "+", "3", "*"]
s = Solution()
print(s.main(nums))
