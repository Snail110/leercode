class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 递归 反转左右子节点即可
# class Solution:
#     def reverseTree(self,root:TreeNode):
#         """
#         递归 反转左右子节点即可
#         :param root:
#         :return:
#         """
#         if root == None:
#             return root
#
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp
#
#         self.reverseTree(root.left)
#         self.reverseTree(root.right)
#
#         return root

# 迭代 栈
class Solution:
    def reverseTree(self,root:TreeNode):
        """
        迭代 栈 反转左右子节点即可
        :param root:
        :return:
        """
        vec = []
        vec.append(root)
        while len(vec) > 0:
            node = vec.pop()

            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.left:
                vec.append(node.left)
            if node.right:
                vec.append(node.right)

        return root

root = TreeNode(1);root.left = TreeNode(3);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)

s = Solution()

r = s.reverseTree(root)
print(r.value,r.left.value,r.right.value,r.left.left.value,r.left.right.value)
