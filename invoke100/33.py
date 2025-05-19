class Solution:
    def search(self, nums:list[int], target:int) ->int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right+1)//2
                if target == nums[mid]:
                    return mid
                if nums[mid] >= nums[0]:
                    if nums[0] <= target and target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target and target <= nums[len(nums)-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
        
            return -1

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums,target))