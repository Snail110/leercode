"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例： 给定二叉树 [3,9,20,null,null,15,7]，
解法：递归法，迭代法，层级遍历
"""

from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 递归法
class Solution:
    def maxDepth(self,root:TreeNode):
        """
        :param root:
        :return:depth
        """
        if root == None:
            return 0
        depth_left = 0
        depth_right = 0
        if root.left:
            depth_left = self.maxDepth(root.left)
        if root.right:
            depth_right = self.maxDepth(root.right)
        depth = 1 + max(depth_left, depth_right)
        return depth


# 迭代法
class Solution2:
    def maxDepth(self,root:TreeNode):
        """
        层序遍历
        :param root:
        :return: depth
        """
        if root== None:
            return 0
        d = deque([root]) # 初始化
        depth = 0
        while(d):
            size = len(d) # 先统计右多少个节点
            for i in range(size):
                cur = d.popleft() # 每遍历一个节点就吐出一个，然后塞进2个子
                if cur.left:
                    d.append(cur.left)
                if cur.right:
                    d.append(cur.right)
            depth += 1
        return depth





root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(7)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(5);root.right.right = TreeNode(8)

root.left.left.left = TreeNode(1);root.left.left.right = TreeNode(3)

# s = Solution()
# print(s.maxDepth(root))

s = Solution2()
print(s.maxDepth(root))