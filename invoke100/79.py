class Solution:
    def main(self,board,word):
        m = len(board[0])
        n = len(board)
        ans = []
        visited = [[False] * m for _ in range(n)]

        def dfs(visited,i,j,index):
            # 超过边界，遍历过，当前元素不想等
            if i < 0 or i > n-1 or j < 0 or j > m-1 or visited[i][j] or word[index] != board[i][j]:
                return 
            # 如果当前元素想等，说明有
            if index == len(word)-1:
                ans.append(True)
                return 
            # 赋值 是否遍历
            visited[i][j] = True
            # 四个遍历方向 index记录遍历多少次
            dfs(visited,i-1,j,index+1)
            dfs(visited,i+1,j,index+1)
            dfs(visited,i,j-1,index+1)
            dfs(visited,i,j+1,index+1)
            # 退出来
            visited[i][j] = False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    dfs(visited,i,j,0)
        return len(ans) > 0
    def main1(self,board,word):
        def dfs(i,j,index):
            if not (0<=i<=n-1) or not (0<=j<=m-1) or board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[i][j] = '' # 遍历过的赋值为空
            res = dfs(i,j-1,index+1) or dfs(i,j+1,index+1) or dfs(i+1,j,index+1) or dfs(i-1,j,index+1)
            board[i][j] = word[index]
            return res
        
        m = len(board[0])
        n = len(board)
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False

s = Solution()
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','D']]
word = 'ABCCED'
print(s.main1(board,word))