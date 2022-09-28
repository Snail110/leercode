"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。
思路
这道题目要求从根节点到叶子的路径，所以需要前序遍历，这样才方便让父节点指向孩子节点，找到对应的路径。

在这道题目中将第一次涉及到回溯，因为我们要把路径记录下来，需要回溯来回退一一个路径在进入另一个路径。

前序遍历以及回溯的过程如图：

我们先使用递归的方式，来做前序遍历。要知道递归和回溯就是一家的，本题也需要回溯。

回溯和递归是一一对应的，有一个递归，就要有一个回溯

"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def traversal(self,root:TreeNode,path:list,result:list):
        """
        前序遍历
        :param root:
        path：当前路径string，result：全部遍历的路list
        :return: 无返回值
        """
        # 中，节点值
        path.append(str(root.value))
        # 终止条件 叶子节点就终止了
        if root.left == None and root.right == None:
            spath = '->'.join(path) # string
            result.append(spath)
            return

        # 左
        if root.left:
            # 递归
            self.traversal(root.left,path,result)
            # 回溯
            path.pop()
        # 右
        if root.right:
            # 递归
            self.traversal(root.right,path,result)
            # 回溯 一个递归，一个回溯，不分开
            path.pop()

    def treePath(self,root:TreeNode):
        path = []
        result = []
        self.traversal(root,path,result)
        return result


root = TreeNode(6)

root.left = TreeNode(4);root.right = TreeNode(4)

root.left.left = TreeNode(1);root.left.right = TreeNode(1)


s = Solution()
print(s.treePath(root))