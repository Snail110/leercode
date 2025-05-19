class Solution:
    def permute(self,nums):
        if not nums:
            return -1
        def dfs(nums,res,used):
            if len(res) == len(nums):
                ans.append(res[::])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                res.append(nums[i])
                dfs(nums,res,used)
                used[i] =False
                res.pop()
        ans = []
        res = []
        used = [False] * len(nums)
        dfs(nums,res,used)
        return ans
        
s = Solution()
nums=[1,2,3]
print(s.permute(nums))