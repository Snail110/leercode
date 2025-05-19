class Solution:
    def main(self,nums):
        if not nums:
            return []
        ans = []
        def dfs(index,path):
            ans.append(path[::])
            for i in range(index,len(nums)):
                path.append(nums[i])
                # 注意是I+1b不是index+1，因为要往下寻找i之后的数据 与全排列区分开
                dfs(i+1,path)
                path.pop()
        path = []
        dfs(0,path)
        return ans

s = Solution()
nums = [1,2,3]
print(s.main(nums))