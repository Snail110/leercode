class Solution:
    def main(self,nums):
        nums.sort()
        ll = len(nums)
        ans = []
        path = []
        def dfs(index,path):
            ans.append(path[::])
            if len(path) == ll:
                return 
            # 从index开始是因为要限制不走回头路，一直往后作为起点。
            for i in range(index,ll):
                # 从index开始算起，是因为往下迭代要计算保证同层之间没有重复
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()

        dfs(0,path)
        return ans 

s = Solution()
nums = [1,2,2,2]
print(s.main(nums))

