"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:  给定如下二叉树，以及目标和 sum = 22，


递归：深度优先遍历的
递归函数什么时候需要返回值？什么时候不需要返回值？这里总结如下三点：
如果需要搜索整棵二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是本文下半部分介绍的113.路径总和ii）
如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值。 （这种情况我们在236. 二叉树的最近公共祖先 (opens new window)中介绍）
如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（本题的情况）

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def pathNodeSum(self,root:TreeNode,cont:int):
        """
        递归 + 回溯
        :param root:
        :param cont: sum
        :return: bool
        """
        if root == None:
            return False
        # 终止条件 遍历到叶子节点 cont递减到0返回True or False
        if root.left == None and root.right == None and cont == 0:
            return True
        if root.left == None and root.right == None and cont != 0:
            return False

        # 单层逻辑
        if root.left:
            #减去left value
            cont = cont - root.left.value
            # 递归
            if self.pathNodeSum(root.left, cont):
                return True
            # 回溯
            cont = cont + root.left.value
        if root.right:
            # 减去right value
            cont = cont - root.right.value
            # 递归 为啥有返回值
            if self.pathNodeSum(root.right, cont):
                return True
            # 回溯
            cont = cont + root.right.value
        # 没有返回True 要返回False
        return False

    def isFlag(self,root:TreeNode, cont:int):
        cont = cont - root.value
        return self.pathNodeSum(root, cont)


root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(4);root.left.right = TreeNode(1)

root.left.left.left = TreeNode(1)
cont = 15
s = Solution()
print(s.isFlag(root,cont))