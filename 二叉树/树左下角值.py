class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 层序遍历
# class Solution:
#     def leftValue(self,root:TreeNode):
#         if root == None:
#             return
#         # 队列
#         vec = []
#         # 最终保存值
#         result = []
#
#         vec.append(root)
#         while len(vec):
#             res = []
#             size = len(vec)
#             for i in range(size):
#                 node = vec.pop(0)
#                 res.append(node)
#                 if node.left:
#                     vec.append(node.left)
#                 if node.right:
#                     vec.append(node.right)
#             result.append(res[0].value)
#         return result


class Solution:
    def maxLeftValue(self,root:TreeNode,maxDepth:int,maxDepthValue:int,depth:int):
        """
        递归 前序遍历 深度优先搜索
        :param root:
        :param maxDepth:
        :param maxDepthValue:
        :return: 无返回值
        """
        # 终止条件 叶子节点 并且赋值
        if root.left != None and root.left.right == None and root.left.left == None:
            if depth > maxDepth:
                maxDepth = depth
                maxDepthValue += root.left.value

        # 确定单层递归逻辑
        if root.left:
            depth += 1
            maxDepthValue = self.maxLeftValue(root.left, maxDepth, maxDepthValue, depth)
            depth -= 1

        if root.right:
            depth += 1
            maxDepthValue = self.maxLeftValue(root.right, maxDepth, maxDepthValue, depth)
            depth -= 1

        return maxDepthValue

    def main(self,root:TreeNode):
        if root == None:
            return
        maxDepth = -1
        maxDepthValue = -1
        depth = 0
        maxDepthValue = self.maxLeftValue(root,maxDepth,maxDepthValue,depth)
        return maxDepthValue

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)
root.left.left = TreeNode(4);root.left.right = TreeNode(7)

s = Solution()
print(s.main(root))