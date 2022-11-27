"""
lc：10002 查找常用字符
给定仅有小写字母组成饿字符串数组A，返回列表重的每个字符串都显示的全部字符串列表
小写字母，出现频率-》哈希

A = ['bella','label','roller']
输出：['e','l','l']
主要是公用的字符，那么该字符取决于最少公用的频率
"""

class Solution:
    def common_str(self,A:list):
        """

        :param A:
        :return:
        """
        def index_a(s):
            return ord(s) - ord('a')

        hash_a = [0] * 26
        a = A[0]
        for i in a:
            hash_a[index_a(i)] += 1

        for other in A[1:]:
            hash_others = [0] * 26
            for j in other:
                hash_others[index_a(j)] += 1
            for m in range(len(hash_a)):
                hash_a[m] = min(hash_a[m],hash_others[m])
        res = []
        for index in range(len(hash_a)):
            c = hash_a[index]
            while c:
                s = chr(ord('a') + index)
                res.append(s)
                c -= 1
                
        return res

A = ['bella','label','roller']
s = Solution()
print(s.common_str(A))