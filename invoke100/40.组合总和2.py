class Solution:
    def combinationSum2(self, nums, target):

        def dfs(nums,target,left,res):
            if sum(res) > target:
                return 
            elif sum(res) == target:
                ans.append(res[::])
                return 
            for i in range(left,len(nums)):
                # i >left 从left之后算起，如果有重复，那么跳过
                if i >left and nums[i] == nums[i-1]:
                    continue
                res.append(nums[i])
                dfs(nums,target,i+1,res)
                res.pop()
        res = []
        ans = []
        nums.sort()
        dfs(nums,target, 0, res)
        return ans
s = Solution()
nums = [10,1,2,7,6,1,5]
target = 8
nums = [2,5,2,1,2]
target = 5
print(s.combinationSum2(nums,target))