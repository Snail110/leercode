class Solution:
    def searchInsert(self, nums:list[int], target:int) ->int:
        l = len(nums)
        left = 0
        right = l - 1
        res = l-1
        while left <=right:
            mid = (left + right+1)//2
            if nums[mid] >= target:
                right = mid -1
                res = mid
            else:
                left = mid + 1
        return res

s = Solution()
nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
nums = [1,3,5,6]
target = 0
print(s.searchInsert(nums,target))