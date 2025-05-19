class Solution:
    def lenghtOfLastWord(self,s):
        low = 0
        fast = 0
        max_len = 0
        while fast < len(s):
            if s[fast] == ' ':
                low = fast + 1
            elif fast == len(s) -1:
                max_len = fast - low + 1 
            fast += 1
        return max_len

s = Solution()
str = 'helo dd  worldd'
print(s.lenghtOfLastWord(str))