class Solution:
    def combinationSum(self, nums, target):
        res = []
        ans = []
        def dfs(nums,target,left,res):
            if sum(res) > target:
                return 
            elif sum(res) == target:
                ans.append(res[::])
                return 
            for i in range(left,len(nums)):
                res.append(nums[i])
                dfs(nums,target,i,res)
                res.pop()
        dfs(nums,target, 0, res)
        return ans
s = Solution()
nums = [2,3,6,7]
target = 7
nums = [2,3,5]
target = 8
print(s.combinationSum(nums,target))