"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""

class Solution:
    def threeSum(self,nums:list):
        if len(nums) < 3:
            return []
        nums_sort = sorted(nums) # 升序排序
        if nums_sort[0]>0:
            return []

        ans = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            # 第一处去重的地方，对i进行去重复[-2, 0, 0, 2, 2]这种无效，因为在内层的重复。
            if (i>=1 and nums_sort[i]==nums_sort[i-1]):
                continue
            while(left<right):
                # 前面两种情况不用去重，因为不会进行记录
                if (nums_sort[i] + nums_sort[left] + nums_sort[right]>0):
                    right -= 1
                elif (nums_sort[i] + nums_sort[left] + nums_sort[right]<0):
                    left += 1
                else:
                    ans.append([nums_sort[i],nums_sort[left],nums_sort[right]])
                    # 第二处利用while 对left和right的重复
                    while left != right and nums_sort[left] == nums_sort[left+1]: left += 1
                    while left != right and nums_sort[right] == nums_sort[right-1]: right -= 1
                    left += 1
                    right -= 1
        return ans
nums = [-2, -2,  0, 2, 2] # [0, 0, 0, 0] # [-2, 0, 0, 2, 2]
s = Solution()
print(s.threeSum(nums))



