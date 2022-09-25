class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def leftYeZi(self,root:TreeNode):
        """
        后序遍历
        :param root:
        :return:
        """
        if root == None:
            return 0
        # 左节点的左叶子节点值
        leftValue = self.leftYeZi(root.left)
        # 右节点的左叶子节点值
        rightValue = self.leftYeZi(root.right)
        # 中
        minValue = 0
        # 判断何为左叶子节点
        if root.left != None and root.left.left == None and root.left.right == None:
            minValue = root.left.value

        return leftValue + rightValue + minValue

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)
# root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.leftYeZi(root))