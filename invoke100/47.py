class Solution:
    def permute2(self,nums):
        if not nums:
            return []
        ans = []
        def dfs(nums,res,used,ans):
            if len(res) == len(nums):
                ans.append(res[::])
                return 
            for i in range(len(nums)):
                # 前一个没有用过说明是同层，当前用过说明同路径不需要再次用了
                if (i > 0 and nums[i] == nums[i-1] and not used[i-1]) or used[i]:
                    continue
                used[i] = True
                res.append(nums[i])
                dfs(nums,res,used,ans)
                res.pop()
                used[i] =False
        res = []
        used = [False] * len(nums)
        nums.sort()
        dfs(nums,res,used,ans)
        return ans
s = Solution()
nums = [1,1,2]
print(s.permute2(nums))