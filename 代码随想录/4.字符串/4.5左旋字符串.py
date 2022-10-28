"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

限制：
1 <= k < s.length <= 10000

具体步骤为：

反转区间为前n的子串
反转区间为n到末尾的子串
反转整个字符串
最后就可以得到左旋n的目的，而不用定义新的字符串，完全在本串上操作。

"""

class Solution:
    def reverseString(self,s:str,n:int):

        # 反转字符串
        def reverseWord(s:str,left:int,right:int):
            s_list = list(s)
            while(left<right):
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left += 1
                right -= 1
            return ''.join(s_list)

        lenght = len(s)
        s = reverseWord(s,0,n-1)
        s = reverseWord(s, n, lenght-1)
        s = reverseWord(s,0,lenght-1)
        return s

s = "abcdefg"
k = 2
s_ = Solution()
print(s_.reverseString(s,k))

