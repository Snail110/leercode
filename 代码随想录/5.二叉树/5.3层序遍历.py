"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）
层序遍历一个二叉树。就是从左到右一层一层的去遍历二叉树

队列先进先出，符合一层一层遍历的逻辑，而是用栈先进后出适合模拟深度优先遍历也就是递归的逻辑。

而这种层序遍历方式就是图论中的广度优先遍历，只不过我们应用在二叉树上。

使用队列实现二叉树广度优先遍历

"""

from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 迭代法
class Solution1:
    def levelOrder(self,root:TreeNode):
        results = [] # 总存储
        if root == None:
            return []
        que = deque([root]) # 添加节点队列
        while que:
            lenght = len(que) # 遍历队列中所有的节点
            result = [] # 单队列存储
            for i in range(lenght):
                node = que.popleft() # 弹出头部节点
                result.append(node.value) # 存在单层中
                if node.left:
                    que.append(node.left) # 添加下层的左节点
                if node.right:
                    que.append(node.right) # 添加下层的右节点

            results.append(result)
        return results

# 递归法
class Solution2:
    def levelOrder(self,root:TreeNode):
        results = []
        def helper(root:TreeNode,depth:int):
            # 终止条件
            if root == None:
                return []
            # 精华所在：提前创建一个[]占据位置，为后面添加值做准备
            if len(results) == depth:
                results.append([])
            results[depth].append(root.value)
            if root.left:
                helper(root.left,depth + 1)

            if root.right:
                helper(root.right,depth + 1)
        helper(root,0)

        return results



root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(7)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(5);root.right.right = TreeNode(8)

# s = Solution()
# print(s.levelorder(root))

s = Solution2()
print(s.levelOrder(root))
