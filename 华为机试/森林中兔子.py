"""
森林中有未知数量的兔子。提问其中若干只兔子 "还有多少只兔子与你（指被提问的兔子）颜色相同?" ，将答案收集到一个整数数组 answers 中，其中 answers[i] 是第 i 只兔子的回答。

给你数组 answers ，返回森林中兔子的最少数量。

 

示例 1：

输入：answers = [1,1,2]
输出：5
解释：
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/rabbits-in-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def tuzi_num(self,nums:list):
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        res = 0
        for j in d.keys():
            a = d[j]//2
            b = d[j]%2

            res += 2 * j * a + b * (j + 1)
        return res

nums = [1,1,2]
s = Solution()
print(s.tuzi_num(nums))