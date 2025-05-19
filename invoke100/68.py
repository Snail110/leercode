class Solution:
    def main(self,n):
        left = 0
        right = n
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
s = Solution()
n = 10
print(s.main(n))
