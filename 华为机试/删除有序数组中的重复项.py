"""
给定一个剩序数组nums，原地删除重复出现的元素，使得每个元素只能出现一次。

1、双指针方法
left，right
先让right开始从做往右遍历
if nums[left] = nums[right]:right+=1
else:
left += 1;
nums[left] = nums[right]
right += 1

"""

class Solution:
    def main(self,nums:list):

        left = 0
        right = 0
        len_ = len(nums)
        while right < len_:
            if nums[right] == nums[left]:
                right += 1

            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return nums[:left+1]

s = Solution()
nums = [1,1,2,3,3,3]
print(s.main(nums))