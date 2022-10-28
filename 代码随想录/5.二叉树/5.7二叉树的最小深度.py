"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

返回它的最小深度 2
"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def minDepth(self,root:TreeNode):
        """

        :param root:
        :return: depth
        """
        if root == None:
            return 0
        #说明下面root就不是None
        # 左
        depth_right = self.minDepth(root.right)
        # 右
        depth_left = self.minDepth(root.left)
        # 中 1 + 就是求中
        if root.right != None:
            return depth_right + 1
        if root.left != None:
            return depth_left + 1
        depth = 1 + min(depth_left,depth_right)
        return depth
root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(1)


s = Solution()
print(s.minDepth(root))

