class Solution:
    def searchRange(self, nums:list[int], target:int) ->int:
        def binaryRange(nums,target,lower):
            left = 0
            right = len(nums) - 1
            res = len(nums)
            while left <= right:
                mid = (left + right+1)//2
                # 大于tarfget 和 等于target第一个值
                if nums[mid] > target or (lower and nums[mid]>=target):
                    right = mid - 1
                    res = mid
                else:
                    left = mid + 1
            return res
        left = binaryRange(nums,target,True)
        right = binaryRange(nums,target,False) -1
        if not (nums[left] == target and nums[right] == target):
            return [-1,-1]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums,target))