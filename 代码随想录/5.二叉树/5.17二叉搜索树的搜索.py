"""
二叉搜索树的搜索
"""

class TreeNode:
    def __init__(self,value:None):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def searchValue(self,root:TreeNode,value:int):
        """
        二叉搜索树的左边子树小于节点，右边子树大于节点
        :param root:
        :param value:
        :return:
        """
        # 终止条件 没找到和找到了返回
        if root == None or root.value == value:
            return root

        if value > root.value:
            # 要有返回值，及时返回
            root = self.searchValue(root.right,value)
        if value < root.value:
            # 要有返回值，及时返回
            root = self.searchValue(root.left, value)
        return root
root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(3)

root.right.left = TreeNode(0);root.right.right = TreeNode(7)

s = Solution()
print(s.searchValue(root,3).value)