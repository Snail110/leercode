"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:  给定如下二叉树，以及目标和 sum = 22

"""
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
# 112 路径总和
class Solution:
    def path_sum_equal_target(self,root:TreeNode,res:int,target:int):
        """

        :param root:
        :param res:
        :param target:
        :return:
        """
        # 前序遍历
        if root.right is None and root.left is None and res == target:
            return True
        if root.right is None and root.left is None and res != target:
            return False

        if root.left:
            res += root.left.value
            if self.path_sum_equal_target(root.left,res,target):
                return True
            res -= root.left.value

        if root.right:
            res += root.right.value
            if self.path_sum_equal_target(root.right,res,target):
                return True
            res -= root.right.value

        return False

    def main(self,root:TreeNode,target:int):
        if root is None:
            return False
        res = root.value
        flag = self.path_sum_equal_target(root,res,target)
        return flag
root = TreeNode(1);root.right = TreeNode(2);root.left = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
count = 10
print(s.main(root,count))