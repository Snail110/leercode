"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

例如:

输入: A = [ 1, 2] B = [-2,-1] C = [-1, 2] D = [ 0, 2] 输出: 2 解释: 两个元组如下:

    (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution:
    def fourNumberSum2(self,A:list,B:list,C:list,D:list):
        ab_dict = dict() # 存储A+B的值和出现的次数

        for a in A:
            for b in B:
                if (a+b) in ab_dict:
                    ab_dict[a+b] += 1
                else:
                    ab_dict[a+b] = 1
        count = 0 # 记录C+D + A+B的次数
        for c in C:
            for d in D:
                if 0-(c+d) in ab_dict:
                    count +=ab_dict[0-(c+d)]
        return count

s= Solution()

A = [ 1, 2,3]
B = [-2,-1,0]
C = [-1, 2,1]
D = [ 0, 2,-1]

print(s.fourNumberSum2(A,B,C,D))

