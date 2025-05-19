class Solution:
    def main(self,n):
        if n <=1:
            return 1
        path = [-1] * (n+1)
        path[0] = 1
        path[1] = 1
        for i in range(2,n+1):
            path[i] = path[i-1] + path[i-2]
        return path[n]

s = Solution()
n = 3
print(s.main(n))