"""
翻转一棵二叉树。

前序遍历，遍历的过程中去翻转每一个节点的左右孩子就可以达到整体翻转的效果。

注意只要把每一个节点的左右孩子翻转一下，就可以达到整体翻转的效果

"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


# 递归
class Solution:
    def swapTree(self,root:TreeNode):
        # 输入参数和输出参数：root
        # 终止条件：root==None
        if root == None:
            return root
        def helper(cur:TreeNode):
            if cur == None:
                return
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            helper(cur.left)
            helper(cur.right)
        helper(root)
        return root

# 迭代
class Solution1:
    def swapTree(self,root:TreeNode):
        # 输入参数和输出参数：root
        # 终止条件：root==None
        if root == None:
            return root
        st = [] # 栈
        st.append(root) # 添加根节点
        while(st):
            cur = st.pop()
            cur.right,cur.left = cur.left,cur.right
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        return root


"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left #中
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root
"""
root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(7)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(5);root.right.right = TreeNode(8)

# s = Solution()
# r = s.swapTree(root)


s1 = Solution1()
r1 = s1.swapTree(root)

print(r1.left.left.value)