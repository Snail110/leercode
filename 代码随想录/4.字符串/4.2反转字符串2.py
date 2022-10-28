"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

说白了就是 每个k个反转k个字符，剩下的反转
示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg
"""

class Solution:
    def reverse2(self,s:str,k:int):

        def reverse(s_list:list):
            left = 0
            right = len(s_list) - 1
            while(left<right):
                tmp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = tmp
                left += 1
                right -= 1
            return ''.join(s_list)
        res = list(s)
        # list 列表超出长度，也不会报错，会自动显示到到最末尾值，
        for i in range(0,len(res),2*k):
            res[i:k] = reverse(res[i:k])

        return ''.join(res)

s = "abcdefg"
k = 2
s_ = Solution()
print(s_.reverse2(s,k))
