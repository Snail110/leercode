"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

贪心算法：

"""

class Solution:
    def jump_tanxin(self,nums:list):
        """
        贪心算法，每次找到最大范围，如果达到了最大范围，jump+=1.一直到达最终位置
        :param nums:
        :return:
        """
        max_step = 0 # 下一次最大范围
        jump = 0 # 步数
        end = 0 #当前的最大范围
        n = len(nums)
        for i in range(n-1):
            max_step = max(max_step,nums[i] + i)
            # 到达当前最大范围
            if i == end:
                jump += 1   # 步数+1
                end = max_step # 更新最大范围
            if end == n-1:
                break

        return jump

s = Solution()
nums = [0]
print(s.jump_tanxin(nums))


