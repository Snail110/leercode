"""
利用二叉树的性质：
根据中序遍历后，数组为单调递增数组
"""

class TreeNode:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

# class Solution:
#     def __init__(self, pre, min_abs):
#         self.pre = pre
#         self.min_abs = min_abs
#
#     def minAbsValue(self, root: TreeNode):
#
#         if root is None:
#             return True
#
#         # 左
#         self.minAbsValue(root.left)
#         # 中 判断pre不为空
#         if self.pre:
#             self.min_abs = min(self.min_abs, root.value - self.pre.value)
#
#         self.pre = root  # 交换前一个位置
#         # 右
#         self.minAbsValue(root.right)
#
#     def res(self,root:TreeNode):
#         self.minAbsValue(root)
#         return self.min_abs

class Solution:
    def minAbsValue(self,root:TreeNode,vec:list):
        if root is None:
            return vec

        # 左
        if root.left:
            vec = self.minAbsValue(root.left,vec)
        # 中
        vec.append(root.value)
        # 右
        if root.right:
            vec = self.minAbsValue(root.right,vec)

        return vec

    def result(self,root:TreeNode):
        if root is None:
            return []
        vec = []
        vec = self.minAbsValue(root,vec)
        min_value = 2 ** 32
        for i in range(1,len(vec)):
            min_value = min(min_value,vec[i] - vec[i-1])
        return min_value


root = TreeNode(2);root.left = TreeNode(1);root.right = TreeNode(4)

root.right.left = TreeNode(3);root.right.right = TreeNode(7)

s = Solution()
print(s.result(root))

