"""
654 构建最大二叉树
根为最大元素
左子树为最大值左边构造的
右子树是最大值右边构建的
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def splitList(self, res: list, value: int):
        """
        分割list
        :param res:
        :param value:
        :return:
        """
        for i in range(len(res)):
            if res[i] == value:
                return res[:i], res[i + 1:]

    def buildMaxTree(self, preOrder: list):
        if len(preOrder) == 0:
            return
        max_value = max(preOrder)
        root = TreeNode(max_value)
        left_tree, right_tree = self.splitList(preOrder, max_value)

        root.left = self.buildMaxTree(left_tree)
        root.right = self.buildMaxTree(right_tree)

        return root

s = Solution()
preOrder = [3,2,1,6,0,5]
root = s.buildMaxTree(preOrder)
print(root.value,root.left.value,root.left.right.value)
