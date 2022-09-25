class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 层序遍历
# class Solution:
#     def nodeSum(self,root:TreeNode):
#         if root == None:
#             return 0
#         vec = []
#         node_count = 0
#         vec.append(root)
#         while len(vec) > 0:
#             node = vec.pop(0)
#             node_count += 1
#             if node.left:
#                 vec.append(node.left)
#             if node.right:
#                 vec.append(node.right)
#
#         return node_count

# 递归后序遍历
# 将每一个二叉树的节点数作为返回值，不断地递归便利
class Solution:
    def nodeSum(self,root:TreeNode):

        if root == None:
            return 0

        return self.nodeSum(root.right) + self.nodeSum(root.left) + 1

root = TreeNode(1);root.right = TreeNode(2);root.left = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()

print(s.nodeSum(root))