class Solution:
    def nextPermutation(self, nums:list[int]) -> list:
        l = len(nums)
        i = 0 
        j = 0
        k = 0
        # 获取最后的第一个相邻增序的索引i，j
        for n in range(l-1,0,-1):
            if n > 1 and nums[n-1]<nums[n]:
                i = n - 1
                j = n
                break
            # elif n == 1:
            #     nums.sort()
            #     return nums
        # 获取最小大于nums[i]的nums[k]
        max_diff = 2**23
        for m in range(i,l):
            if nums[m] - nums[i] > 0 and nums[m] - nums[i] < max_diff :
                max_diff = nums[m] - nums[i]
                k = m
        nums[i],nums[k] = nums[k],nums[i]
        # 从j开始反转降序队列
        for o in range(j,(l+j+1)//2):
            nums[o],nums[l-(o-j+1)] = nums[l-(o-j+1)],nums[o]
        return nums


s = Solution()
nums = [4,3,2,1]
nums = [1,1,5]
nums = [1,2,3]
print(s.nextPermutation(nums))