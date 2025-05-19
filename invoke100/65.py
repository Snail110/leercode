class Solution:
    def main(self,digits):
        ll = len(digits)
        pre = 0
        ans = []
        a = digits.pop()
        if a + 1 ==10:
            pre = 1
            a = 0
        else:
            a = a + 1
        ans.append(a)
        while digits:
            a = digits.pop() + pre
            if a == 10:
                pre = 1
                a = 0
            else:
                pre = 0
            ans.append(a)
        if pre ==1:
            ans.append(1)
        return ans[::-1]

s = Solution()
print(s.main([9,9,9]))