"""
每个2k字符，反转前k字符，
如果剩余字符少于k个，则全部反转，
如果剩余字符小于2k，反转前k个。

s = 'abcdefg',k=2
s = 'bacdfeg'

"""

class Solution:
    def reverse_str(self,s:str,k:int):
        """
        :param s:
        :return:
        """
        len_ = len(s)
        m = len_ // (2 * k)
        s_list = list(s)
        for i in range(m+1):
            l = 2*k*i
            r = min(2*k*i + k-1,len_ - 1)
            while l < r:
                s_list[l],s_list[r] = s_list[r],s_list[l]
                l += 1
                r -= 1
        return ''.join(s_list)

# class Solution:
#     def reverse_str(self,s:str,k:int):
#         s_list = list(s)
#         len_ = len(s_list)
#         if k >= len_:
#             return s_list[::-1]
#         for i in range(0,len_,2*k):
#             s_list[i:i+k] = s_list[i:i+k][::-1]
#
#         return ''.join(s_list)

s_str = '0123456789'
s = Solution()
print(s.reverse_str(s_str,3))



