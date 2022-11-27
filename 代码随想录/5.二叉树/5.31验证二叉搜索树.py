class TreeNode:
    def __init__(self,value:None):
        self.value = value
        self.left = None
        self.right = None

# class Solution:
#     """
#     左子树所有值都小于节点，右子树所有值都大于节点
#     左子树也是搜索二叉树，右子树也是搜索二叉树
#     按照中序遍历，生成数组，该数组必须是单调递增数组，才能证明是二叉搜索树
#     """
#     def mid_tree(self,root:TreeNode,vec:list):
#         if root is None:
#             return vec
#         if root.left:
#             vec = self.mid_tree(root.left,vec)
#         vec.append(root.value)
#         if root.right:
#             vec = self.mid_tree(root.right,vec)
#         return vec
#
#     def is_up_nums(self, root:TreeNode):
#         vec = []
#         vec = self.mid_tree(root,vec)
#         for i in range(1,len(vec)):
#             if vec[i] <= vec[i-1]:
#                 return False
#         return True

class Solution:
    def isSearchTree(self,root:TreeNode,max_value:-2**32):
        """
        二叉搜索树需要中序遍历，因为中序遍历可以将树写成单调递增的数组
        然后利用前一个节点必定小于后一个节点的特征，判断是否是二叉搜索树
        :param root:
        :return:
        """

        if root is None:
            return True

        left = self.isSearchTree(root.left,max_value)   # 左

        if root.value > max_value:
            max_value = root.value  # 中
        else:
            return False

        right = self.isSearchTree(root.right,max_value)     # 右

        return left and right

root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(4)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()

max_value = -2 ** 32
print(s.isSearchTree(root,max_value))