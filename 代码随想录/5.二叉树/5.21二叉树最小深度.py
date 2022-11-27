class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def minDepth(self,root:TreeNode):
        """
        后序遍历
        :param root:
        :return:
        """
        if root == None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if root.left == None and root.right:
            return right_depth + 1
        if root.left and root.right == None:
            return left_depth + 1

        depth = min(left_depth, right_depth) + 1
        return depth


root = TreeNode(1);root.right = TreeNode(2);root.left = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
# root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.minDepth(root))


