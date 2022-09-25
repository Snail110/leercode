from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
        self.word = ''

    def insert(self, word: str) -> None:
        """
        :param word:
        :return:
        """
        node = self  # 定义node的类型
        for ch in word:
            # 增加当前node的子节点
            node = node.children[ch]
        node.isEnd = True
        node.word = word


class Solution:
    def findWord(self,board:list,words:list):
        # 创建 词典树
        T = TrieNode()
        for word in words:
            T.insert(word)

        ans = []
        m,n = len(board),len(board[0])
        def dsp(i,j,now:TrieNode):
            # 终止条件 网格中的字符不在词典子节点中
            if board[i][j] not in now.children:
                return
            # 获取当前board的字符
            ch = board[i][j]
            # 获取当前词典树中对应的字符 向下搜索
            now = now.children[ch]
            # 当当前的节点word不为空，说明是一个完整的字
            if now.word != '':
                ans.append(now.word)
            # 掩盖其当前路径搜索过的字符
            board[i][j] = '#'
            # 本身赋值 已经回溯
            for (i1,j1) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:

                if i1 >= 0 and i1 < m and j1 >=0 and j1 < n:
                    dsp(i1,j1,now) # 已经包含搜索和回溯
            board[i][j] = ch # 回溯
        # 分别遍历所有的网格字符
        for i in range(m):
            for j in range(n):
                dsp(i,j,T)
        return ans
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]

words = ['oath','pea','eat','rain']

t = TrieNode()
s = Solution()
print(s.findWord(board,words))

