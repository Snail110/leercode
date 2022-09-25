"""
617
将两个二叉树合并，都有节点，将节点值相加，一方没有节点，默认为0，双方都没节点，则为None

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def addTree(self,root1:TreeNode,root2:TreeNode):

        if root1 == None and root2 == None:
            return
        value = 0
        if root1 == None and root2 != None:
            value = root2.value
        if root1 != None and root2 == None:
            value = root1.value
        if root1 != None and root2 != None:
            value = root1.value + root2.value

        root = TreeNode(value)
        if root1.left == None and root2.left != None:
            root1.left = TreeNode(0)

        elif root1.left != None and root2.left == None:
            root2.left = TreeNode(0)

        elif root1.right == None and root2.right != None:
            root1.right = TreeNode(0)

        elif root1.right != None and root2.right == None:
            root2.right = TreeNode(0)
        elif root1.left != None and root2.left != None and root1.right != None and root2.right != None:
            root.left = self.addTree(root1.left, root2.left)
            root.right = self.addTree(root1.right, root2.right)

        return root

root1 = TreeNode(1);root1.left = TreeNode(2);root1.right = TreeNode(2)
root2 = TreeNode(1);root2.left = TreeNode(2)

s = Solution()
root3 = s.addTree(root1,root2)
print(root3.value,root3.left.value,root3.right.value)
