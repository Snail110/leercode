class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



class Solution:
    def bfs(self,root:TreeNode):
        if root == None:
            return []

        # 定义双队列
        vec = []
        # 定义输出list
        result = []
        # 添加根节点
        vec.append(root)
        index = True
        while len(vec)>0:
            # 定义层list
            res = []
            size = len(vec)
            for i in range(size):
                node = vec.pop(0)
                if index:
                    res.append(node.value)
                else:
                    res.insert(0,node.value)
                if node.left:
                    vec.append(node.left)
                if node.right:
                    vec.append(node.right)
            index = not index
            result.append(res)
        return result

root = TreeNode(1);root.left = TreeNode(3);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(5);root.left.right = TreeNode(6)

s = Solution()
print(s.bfs(root))

