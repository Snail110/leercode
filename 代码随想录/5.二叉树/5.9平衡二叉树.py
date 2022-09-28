"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7

"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root:TreeNode):
        """

        :param root:
        :return: maxdepth
        """
        # 终止条件
        if root == None:
            return 0
        # 统计左孩子的最大深度
        leftDepth = self.maxDepth(root.left)
        if leftDepth == -1:
            return -1
        # 统计左孩子的最大深度
        rightDepth = self.maxDepth(root.right)
        if rightDepth == -1:
            return -1
        
        if abs(leftDepth - rightDepth) > 1:
            return -1

        return 1 + max(leftDepth, rightDepth)


    def isBalance(self,root:TreeNode):
        isbalance = self.maxDepth(root)

        if isbalance != -1:
            return True
        else:
            return False

root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(1)


s = Solution()
print(s.isBalance(root))