"""
二搜索叉树的最近公共祖先 和二叉树的最近公共祖先
1、求最小公共祖先，需要从底向上遍历，那么二叉树只能后序遍历，（回溯从低向上）的遍历方式
2、在回溯中，必然遍历整个二叉树，既然找到了结果，依然需要把其他的节点遍历完，因为要使用递归函数的返回值，来逻辑判断
3、要理解返回值left为空，right不为空，为什么返回right，为什么可以用返回值right传给上一层结果
"""

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# class Solution:
#     def nearfather(self,root:TreeNode,p,q):
#         """
#         二叉搜索树
#         :param root:
#         :param p:
#         :param q:
#         :return:
#         """
#         while root:
#             if p > root.value and q > root.value:
#                 root = root.right
#
#             elif p < root.value and q < root.value:
#                 root = root.left
#             else:
#                 return root.value

# s = Solution()
# p = 3
# q = 5
# print(s.nearfather(root,3,3))


# 二叉树的最近公共祖先 采用后序遍历的回溯，从下往上遍历，寻找相同的节点

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 关于节点相等，这里需要判断value相等才可以
        if not root or root.value == p.value or root.value == q.value:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        else:
            return root

root = TreeNode(6)
root.right = TreeNode(2);root.left = TreeNode(1)

root.left.left = TreeNode(0);root.left.right = TreeNode(4)
root.right.left = TreeNode(7);root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3);root.left.right.right = TreeNode(5)

p = TreeNode(3)
q = TreeNode(5)
s = Solution()
print(s.lowestCommonAncestor(root,p,q).value)

