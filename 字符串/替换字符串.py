class Solution:
    def tihuan(self,s_str:str):
        s = list(s_str)
        l = []
        for i in s:
            if i != ' ':
                l.append(i)
            else:
                l.append('%20')
        return ''.join(l)

s = Solution()
print(s.tihuan('we are happy !'))
