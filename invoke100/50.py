class Solution:
    def pow(self,x,n):
        def quickMul(n):
            if n == 0 :
                return 1.0
            # 求得减半后的幂次值为y
            y = quickMul(n//2)
            res = y * y if n % 2 == 0 else y * y * x
            return res
        if n < 0:
            x = 1/x
            n = -n
        return quickMul(n)
s = Solution()
print(s.pow(2,-3))