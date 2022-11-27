"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
nums = [1,3,-1,-3,5,3,6,7]
进阶：

你能在线性时间复杂度内解决此题吗？
答：维护一个单调递减队列

"""

class Solution:
    def window_max_nums(self,nums:list,k:int):
        """

        :param nums:
        :param k:
        :return:
        """
        res = []    # 结果
        len_ = len(nums)
        stack = [0] # 维护一个单调递减队列
        # 先求出第一个滑动窗口扽最大值
        for i in range(k):
            if nums[i] >= nums[stack[0]]:
                stack[0] = i
        res.append(nums[stack[0]])
        # 遍历后面的最大值
        for j in range(k,len_):
            while stack and nums[j] > nums[stack[-1]]:
                stack.pop()

            stack.append(j)
            if stack[0] < j-k+1:
                stack.pop(0)
            res.append(nums[stack[0]])
        return res
nums = [1,3,-1,-3,5,3,6,7]
s = Solution()

print(s.window_max_nums(nums,3))
