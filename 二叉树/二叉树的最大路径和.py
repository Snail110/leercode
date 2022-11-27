"""
二叉树的最大路径和
# 递归的方式 先求出左右叶子节点的最大，然后一次不断的传给父节点，然后最后得出最大值
"""
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def tree_path_max_sum(self,root:TreeNode):
        """

        :param root:
        :return:
        """
        # 终止条件
        if root is None:
            return 0

        left_max = max(0, self.tree_path_max_sum(root.left))
        right_max = max(0, self.tree_path_max_sum(root.right))

        return max(left_max,right_max) + root.value

root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(4)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()
print(s.tree_path_max_sum(root))




