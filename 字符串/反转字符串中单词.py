class Solution:
    def delWord(self,s_str:str):
        s = list(s_str)
        l = len(s)

        left = 0
        right = 0
        while s[right] == ' ' and left < l:
            # 对于不确定数量的空格，采用while，在初始的非空格停下来
            right += 1
        for i in range(right, l):
            if s[i-1] == s[i] == ' ':
                # 采用i-1的形式刚好有一个空格，此时如果末尾有空格，就会多一个空格
                continue
            else:
                s[left] = s[i]
                left += 1
        if s[left-1] == ' ':
            return s[:left-1]
        else:
            return s[:left]
    # 反转 按照分隔符 的字符串
    def reverseWord(self,s_str:str):
        s = list(s_str)
        l = len(s)
        left = 0
        right = 0

        while right < l:
            while right < l and s[right] != ' ':
                right += 1
            s[left:right] = s[left:right][::-1]
            right += 1
            left = right
        return s
    def reverseStr(self,s_str:str):

        s = self.delWord(s_str)
        print(s)
        s = s[::-1]
        res = self.reverseWord(s)
        return ''.join(res)

s_str = '  we are    happy'
s = Solution()

print(s.reverseStr(s_str))








