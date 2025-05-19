class Solution:
    def main(self,nums):
        slow = 2
        quick = 2
        ll = len(nums)
        if ll <=2:
            return nums
        while quick < ll:
            if nums[slow-2] != nums[quick]:
                nums[slow] = nums[quick]
                slow += 1
            quick += 1
    
        return nums,slow
    def main(self,nums):
        ll = len(nums)
        slow = 0
        for quick in range(ll):
            # 小于2保留，可以直接赋值，然后slow移动一步，
            # 如果slow前2位值不等于quick值，说明quick已经越过了重复值，需要对slow赋新值，slow移动一位
            if slow < 2 or nums[slow-2] != nums[quick]:
                nums[slow] = nums[quick]
                slow + 1
        return nums

s = Solution()
nums = [0,1,1,2,2,2,2,3,3]
print(s.main(nums))