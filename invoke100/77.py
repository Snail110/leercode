class Solution:
    def main(self,n,k):
        if k ==0:
            return []
        ans = []
        def dfs(index,path):
            if len(path[::]) == k:
                ans.append(path[::])
                return 
            for i in range(index,n+1):
                path.append(i)
                # 注意是i+1是寻找i之后的数据
                dfs(i+1,path)
                path.pop()
        
        path = []
        dfs(1,path)
        return ans

s = Solution()
n = 4
k =2
# n = 1
# k =1
print(s.main(n,k))