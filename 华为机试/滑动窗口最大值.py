"""
寻找滑动窗口的最大值，nums：[1,4,2,2,5,5,5,7],k=3
输出list 每个窗口扽最大值
解法：
双向队列
复杂度：
o（N）
"""

class Solution:
    def window_max_value(self,nums:list,k:int):
        """

        :param nums:
        :return:
        """
        que = []    # 降序排列的双向队列,保存这个index
        res = []    # 保存窗口最大值
        len_ = len(nums)

        for i in range(k):
            if res and nums[i] > res[0]:
                res.append(nums[i])

        for i in range(k-1,len_):
            # 保证 que不为空，并且当前的值大于que最后一个值，那么将最后一个值淘汰，然后知道遇到比当前值大的值
            while que and nums[i] > nums[que[-1]]:
                que.pop()
            # 将当前值加进去
            que.append(i)

            # 如果que的最大值也就是index=0已经超出了窗口范围，那么需要将他淘汰
            if que[0] < i-k+1:
                que.pop(0)  # 淘汰第一个元素最大值
            res.append(nums[que[0]])

        return res

nums = [4,3,5,4,3,3,3,6,7]
k = 3
s = Solution()
print(s.window_max_value(nums,k))


