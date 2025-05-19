class Solution:
    def multipy(self,num1,num2):
        ans = 0
        for i in range(len(num1)):
            res = 0
            div_res = 0
            a = ord(num1[len(num1)-1-i]) - ord('0')
            for j in range(len(num2)):
                b = ord(num2[len(num2)-1-j]) - ord('0')
                mod = a * b % 10
                div = a * b // 10
                res += (mod + div_res) * 10 ** j
                div_res = div
            ans += res * 10 ** i + div_res * 10 ** (i+j+1)
        return ans

s = Solution()
print(s.multipy('99','99'))