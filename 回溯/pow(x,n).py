"""
寻找x的n次幂
"""
class Solution:
    def pow_n(self,x,n):

        if n < 2:
            return x

        if n % 2 == 0:
            return self.pow_n(x,n//2) * self.pow_n(x,n//2)
        else:
            return self.pow_n(x,n//2) * self.pow_n(x,n//2) * x

    def main(self,x,n):
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        return self.pow_n(x,n)

s = Solution()
x = 2
n = -4
print(s.main(x,n))