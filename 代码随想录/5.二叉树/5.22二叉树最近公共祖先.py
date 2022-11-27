"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1: 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 输出: 3 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2: 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 输出: 5 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def near_commmon_parent(self,root:TreeNode,p:int,q:int):
        """

        :param root:
        :param p:
        :param q:
        :return:
        """
        # 终止条件
        if root is None or root.val == q or root.val == q:
            return root

        # 后序遍历

        left = self.near_commmon_parent(root.left,q,p)

        right = self.near_commmon_parent(root.right,p,q)
        # 如果都不为空，说明此时的root是最近公共祖先
        if left != None and right != None:
            return root

        if left == None:
            return right
        if right == None:
            return left
        return None
root = TreeNode(1);root.right = TreeNode(2);root.left = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(3)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.near_commmon_parent(root,4,3).val)