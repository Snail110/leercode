class Solution:
    def main(self,s1,s2,s3):
        n = len(s1)
        m = len(s2)
        p = len(s3)
        if m + n != p:
            return False

        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n+1):
            for j in range(m+1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[n][m]

s = Solution()
s1= 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
print(s.main(s1,s2,s3))