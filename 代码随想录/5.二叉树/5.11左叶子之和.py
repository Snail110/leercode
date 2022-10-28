"""
左叶子之和
首先要注意是判断左叶子，不是二叉树左侧节点，所以不要上来想着层序遍历。

因为题目中其实没有说清楚左叶子究竟是什么节点，那么我来给出左叶子的明确定义：如果左节点不为空，且左节点没有左右孩子，那么这个节点的左节点就是左叶子
后序遍历
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def sumLeftNode(self,root:TreeNode):
        """

        :param root:
        :return: leftsum int
        """

        # 判断终止条件
        if root == None:
            return 0
        # 左
        leftValue = self.sumLeftNode(root.left)
        # 右
        rightValue = self.sumLeftNode(root.right)
        # 中
        midValue = 0
        if root.left and root.left.left == None and root.left.right == None:
            midValue = root.left.value

        return leftValue + rightValue + midValue


root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(1)

root.right.left = TreeNode(1)

s = Solution()
print(s.sumLeftNode(root))