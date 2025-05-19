class Solution:
    def main(self,word1,word2):
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m + n
        
        path = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(m+1):
            path[0][i] = i
        for j in range(n+1):
            path[j][0] = j
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1] == word2[i-1]:
                    tmp = path[i-1][j-1]
                else:
                    tmp = path[i-1][j-1] + 1
                path[i][j] = min(path[i-1][j]+1,path[i][j-1]+1,tmp)
        return path[n][m]

s = Solution()
word1 = 'horse'
word2 = 'ros'
word1 = 'intention'
word2 = 'execution'
print(s.main(word1,word2))
