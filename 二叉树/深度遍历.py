class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def preOrderTrversal(self,root:TreeNode,vec:list):
        """
        前序遍历 递归
        :param vec:
        :return: vec
        """
        # 终止条件
        if root == None:
            return
        vec.append(root.value)
        self.preOrderTrversal(root.left,vec)
        self.preOrderTrversal(root.right,vec)

    def midOrderTrversal(self,root:TreeNode,vec:list):
        """
        中序遍历 递归
        :param vec:
        :return: vec
        """
        # 终止条件
        if root == None:
            return
        self.midOrderTrversal(root.left,vec)
        vec.append(root.value)
        self.midOrderTrversal(root.right,vec)
        return vec

    def midOrderTrversal(self,root:TreeNode,vec:list):
        """
        后序遍历 递归
        :param vec:
        :return: vec
        """
        # 终止条件
        if root == None:
            return
        self.midOrderTrversal(root.left,vec)
        self.midOrderTrversal(root.right,vec)
        vec.append(root.value)

    def main(self,root:TreeNode):
        res = []
        self.midOrderTrversal(root,res)
        return res


root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(3)

root.left.left = TreeNode(4);root.left.right = TreeNode(5)
root.right.left = TreeNode(6);root.right.right = TreeNode(7)

s = Solution()
print(s.main(root))



