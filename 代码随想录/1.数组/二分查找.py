"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

"""

class Solution:
    def two_search(self,nums:list,target:int):
        """

        :param nums:
        :return:
        """
        left = 0
        right = len(nums)
        # 左必右开 < left +1 [left,right)
        while left < right:
            mid = (right - left) // 2 + left
            # 判断条件
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1  # [left,right)
            else:
                return mid

        return -1

nums = [-1,0,3,5,9,12]
target = 12
s = Solution()
print(s.two_search(nums,target))

