class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self,root:TreeNode):
        """
        后序遍历 传入是节点，返回以该界定为根节点的二叉树的高度，如果不是二叉平衡树，则返回-1
        :param root:
        :return:
        """
        if root == None:
            return 0
        # 计算左节点树高度
        left_depth = self.maxDepth(root.left)
        if left_depth == -1:
            return -1
        # 计算右节点树高度
        right_depth = self.maxDepth(root.right)
        if right_depth == -1:
            return -1
        return -1 if abs(left_depth - right_depth) > 1 else max(left_depth,right_depth) + 1


    def main(self,root:TreeNode):
        if self.maxDepth(root) == -1:
            return False
        else:
            return True
root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.main(root))