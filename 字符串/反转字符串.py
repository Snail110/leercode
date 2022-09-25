class Solution:
    def revserStr(self,s_str:str,k:int):
        s = list(s_str)
        l = len(s)
        if k >= l:
            return ''.join(s[::-1])
        for i in range(0,l,2*k):
            s[i:i+k] = s[i:i+k][::-1]

        return ''.join(s)

s_str = '0123456789'
s = Solution()
print(s.revserStr(s_str,2))



