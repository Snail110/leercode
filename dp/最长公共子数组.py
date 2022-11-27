"""
给定两个整数数组A和B，返回两个数组中公共的,长度最长的子数组的长度

# dp[i][j]表示以 i-1结尾的A和以j-1结尾的B的公共的子数组长度dp[i][j]
# 初始化
dp = shape [a+1,b+1]
dp[i][j] = 0

# 递推公式：
if A[i-1] == B[j-1]:
    dp[i][j] = dp[i-1]dp[j-1] + 1

"""
class Solution:
    def max_len_common_sublist(self,A:list,B:list):
        """

        :param A:
        :param B:
        :return:
        """
        # init dp[a][b]才是以len(A)和len(B)结尾的最长长度
        a = len(A) + 1
        b = len(B) + 1
        dp = [[0 for _ in range(a)] for _ in range(b)]

        res = 0
        for i in range(1,a):
            for j in range(1,b):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res,dp[i][j])
        return res
A = [1,2,3,2,1]
B = [3,2,1,4,7]
s = Solution()
print(s.max_len_common_sublist(A,B))