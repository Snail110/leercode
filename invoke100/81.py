class Solution:
    def main(self,nums,target):
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] > nums[right]:
                # 不能写成 target<=nums[mid]，因为mid在下面回+1，-1，就跳过了
                if target >= nums[0] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return False


s = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(s.main(nums,target))
