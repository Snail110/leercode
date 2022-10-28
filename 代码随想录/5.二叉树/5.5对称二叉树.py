"""
给定一个二叉树，检查它是否是镜像对称的。

本题遍历只能是“后序遍历”，因为我们要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否相等。

正是因为要遍历两棵树而且要比较内侧和外侧节点，所以准确的来说是一个树的遍历顺序是左右中，一个树的遍历顺序是右左中。
"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def isSample(self,root:TreeNode):
        """
        递归三部曲
        :param root:
        :return: bool
        """
        def compare(left:TreeNode,right:TreeNode):
            """
            :param left:
            :param right:
            :return: bool
            """
            # 判断终止条件和边界条件 比较2者总共4种可能，但是再相都不为None时，value也有2种情况。
            # 首先排除空节点的情况
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return  False
            elif left == None and right == None:
                return True
            # 排除了空节点，再排除数值不相同的情况
            elif left.value != right.value:
                return False
            # 单层逻辑
            # 外层
            outside = compare(left.left,right.right)
            # 内层
            inside = compare(left.right,right.left)
            return outside and inside

        if root == None:
            return True
        return compare(root.left,root.right)

root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(3);root.right.right = TreeNode(1)

s = Solution()
print(s.isSample(root))
