"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例： 给定二叉树 [3,9,20,null,null,15,7]，

思路：
二叉树的最大深度，凡是求最大深度，最大路径和，都是后续遍历，先求左右节点的值然后处理父节点的值，
一般是递归函数，先求出左右节点的函数值，然后再把父节点加上去

"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def tree_max_depth(self,root:TreeNode):
        """

        :param root:
        :return:
        """

        if root is None:
            # 因为求最大节点，因此空节点应该为0
            return 0
        # 后序遍历，左右节点
        left_depth = self.tree_max_depth(root.left)
        right_depth = self.tree_max_depth(root.right)
        depth = max(left_depth,right_depth) + 1
        return depth

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.tree_max_depth(root))


