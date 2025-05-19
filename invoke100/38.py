class Solution:
    def countAndSay(self, n):
        prev = '1' # 1
        # 从1开始遍历
        for i in range(n-1):
            pos = 0 # 遍历位置
            start = 0 #重复字符开始位置
            cur = '' # 保存当前的ple
            # 遍历当前的数字
            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos +=1
                cur = cur + str(pos-start) + prev[start]
                start = pos
            # 更新当前的prev
            prev = cur
        return prev
s = Solution()
# 1:1
# 2:11
# 3:21
# 4:1211
print(s.countAndSay(n=6))
