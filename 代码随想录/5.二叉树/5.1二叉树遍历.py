"""
每次写递归，都按照这三要素来写，可以保证大家写出正确的递归算法！

确定递归函数的参数和返回值： 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。

确定终止条件： 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。

确定单层递归的逻辑： 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。

"""

# 二叉树的定义
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


# 前序遍历 中左右
class SolutionPre:
    def PreOrderTraversal(self,root:TreeNode):
        # 返回为list
        result = []
        def traversal(root:TreeNode):
            # 终止条件为 root == None
            if root == None:
                return
            # 单层遍历逻辑
            result.append(root.value)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result

# 中序遍历 左中右
class SolutionMid:
    def MidOrderTraversal(self,root:TreeNode):
        result = []
        def traversal(root:TreeNode):
            if root == None:
                return
            traversal(root.left)
            result.append(root.value)
            traversal(root.right)

        traversal(root)
        return result


# 后序遍历 左右中
class SolutionPost:
    def PostOrderTraversal(self, root: TreeNode):
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.value)

        traversal(root)
        return result


root = TreeNode(6)

root.left = TreeNode(4); root.right = TreeNode(7)

root.left.left = TreeNode(1);root.left.right = TreeNode(3)

root.right.left = TreeNode(5);root.right.right = TreeNode(8)

s1 = SolutionPre()
s2 = SolutionMid()
s3 = SolutionPost()

print(s1.PreOrderTraversal(root))
print(s2.MidOrderTraversal(root))
print(s3.PostOrderTraversal(root))