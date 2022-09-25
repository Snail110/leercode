class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 迭代法
# class Solution:
#     def main(self,root:TreeNode):
#         if root == None:
#             return []
#         # 存放结果
#         result = []
#         # 队列
#         vec = []
#         vec.append(root)
#
#         while len(vec) > 0:
#             # 层list
#             res = []
#             size = len(vec)
#             for i in range(size):
#                 node = vec.pop(0)
#                 res.append(node.value)
#                 if node.left:
#                     vec.append(node.left)
#                 if node.right:
#                     vec.append(node.right)
#             result.append(res)
#         return result

# 右视图 199
# class Solution:
#     def main(self,root:TreeNode):
#         if root == None:
#             return []
#         # 存放结果
#         result = []
#         # 队列
#         vec = []
#         vec.append(root)
#
#         while len(vec) > 0:
#             # 层list
#             # res = []
#             size = len(vec)
#             for i in range(size):
#                 node = vec.pop(0)
#                 if i == size - 1:
#                     result.append(node.value)
#                 if node.left:
#                     vec.append(node.left)
#                 if node.right:
#                     vec.append(node.right)
#             # result.append(res[-1])
#         return result


# 二叉树的层平均值 637
# class Solution:
#     def main(self,root:TreeNode):
#         if root == None:
#             return []
#         # 存放结果
#         result = []
#         # 队列
#         vec = []
#         vec.append(root)
#
#         while len(vec) > 0:
#             # 层list
#             res = 0
#             size = len(vec)
#             for i in range(size):
#                 node = vec.pop(0)
#                 res += node.value / size
#                 if node.left:
#                     vec.append(node.left)
#                 if node.right:
#                     vec.append(node.right)
#             result.append(res)
#         return result


# 二叉树的最小深度 111 只有当一个节点的左右子节点都为空，才说明遍历到最底部
class Solution:
    def main(self,root:TreeNode):
        if root == None:
            return []
        # 队列
        vec = []
        vec.append(root)
        depth = 0
        while len(vec) > 0:
            # 层list
            res = 0
            size = len(vec)
            depth += 1
            for i in range(size):
                node = vec.pop(0)
                res += node.value / size
                if node.left:
                    vec.append(node.left)
                if node.right:
                    vec.append(node.right)
                # 最小层最是最先遍历到，因此直接返回就可以，
                if node.left == None and node.right == None:
                    return depth

        return depth

# 递归方法
# class Solution:
#     def pre(self,root:TreeNode):
#         res = []
#         def helper(root,depth):
#             if root == None:
#                 return []
#             if len(res) == depth:
#                 res.append([])
#             res[depth].append(root.value)
#
#             if root.left:
#                 helper(root.left,depth+1)
#             if root.right:
#                 helper(root.right,depth+1)
#
#         helper(root,0)
#         return res


root = TreeNode(1);root.left = TreeNode(3);root.right = TreeNode(2)

root.right.left = TreeNode(4);root.right.right = TreeNode(7)

s = Solution()
print(s.main(root))
