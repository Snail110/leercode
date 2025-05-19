class Solution:
    def main(self,nums):
        stack_1 = []
        stack_2 = []
        stack_0 = []
        for i in nums:
            if i == 0:
                stack_0.append(i)
            elif i == 1:
                stack_1.append(i)
            else:
                stack_2.append(i)
        return stack_0 + stack_1 + stack_2
    def main1(self,nums):
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1
        for j in range(p,len(nums)):
            if nums[j] == 1:
                nums[j],nums[p] = nums[p],nums[j]
                p += 1
        return nums
    def main2(self,nums):
        p = 0
        q = len(nums) - 1
        i = 0
        while i <= q:
            while i <=q and nums[i] == 2:
                nums[i],nums[q] = nums[q],nums[i]
                q -= 1
            if nums[i] == 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1
            i += 1
        return nums
s = Solution()
nums = [1,2,0,2,1,1,0]
print(s.main2(nums))