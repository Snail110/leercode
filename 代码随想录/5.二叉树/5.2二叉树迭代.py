"""
前序遍历是中左右，每次先处理的是中间节点，那么先将根节点放入栈中，然后将 右孩子加入栈，再加入 左孩子。

中序遍历是左中右，先访问的是二叉树顶部的节点，然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点（也就是在把节点的数值放进result数组中），这就造成了处理顺序和访问顺序是不一致的。
那么在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素。

看后序遍历，先序遍历是中左右，后续遍历是左右中，那么我们只需要调整一下先序遍历的代码顺序，就变成中右左的遍历顺序，然后在反转result数组，输出的结果顺序就是左右中了，
"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class SoulutionPre:
    def PreOrderTraversal(self,root:TreeNode):

        if root == None:
            return []
        result = []
        stack = [root]
        # 循环停止条件
        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.right:
                stack.append(node.right)

            # 这里采用串行的if判断，每一步都要走
            if node.left:
                stack.append(node.left)
        return result

class SoulutionMid:
    def MidOrderTraversal(self,root:TreeNode):
        if root == None:
            return []
        result = []
        stack = [] # 不能提前将root放在stack里面
        cur = root
        # 循环停止条件 当前节点和 stack都是空就停止，
        while cur or stack:
            # 先循环到最左边的底层
            if cur:
                stack.append(cur)
                cur = cur.left
            # 采用else 说明是互斥条件
            else:
                # 开始吐节点写进result
                cur = stack.pop()
                result.append(cur.value)
                cur = cur.right

        return result


class SoulutionPost:
    def PostOrderTraversal(self,root:TreeNode):
        if root == None:
            return []
        result = []
        stack = [root] #
        # 循环停止条件 当前节点和 stack都是空就停止，
        while stack:
            # 弹出中间节点
            cur = stack.pop()
            result.append(cur.value)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return result[::-1]


root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(7)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(5);root.right.right = TreeNode(8)

s1 = SoulutionPre()
s2 = SoulutionMid()
s3 = SoulutionPost()

print(s1.PreOrderTraversal(root))
print(s2.MidOrderTraversal(root))
print(s3.PostOrderTraversal(root))