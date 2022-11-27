"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
维护一个单调递减栈，存储当前的索引，然后只要是将要进入的元素大于栈里元素，那么将栈里全部弹出，然后将其塞入
并且栈里元素被弹出的同时，计算索引差值，放在对应ans的索引位置保存。

"""

class Solution:
    def main(self,temperatures:list):
        """"""
        stack = []  # 单调栈，塞入大的元素
        ans = [0] * len(temperatures)   ## 保存插值天数
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)

        return ans

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()
print(s.main(temperatures))