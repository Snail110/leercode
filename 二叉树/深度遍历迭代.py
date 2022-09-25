class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def traversal(self,root:TreeNode):
        """
        前序遍历
        :param root:
        :return:
        """
        vec = []
        res = []
        if root == None:
            return []

        vec.append(root)
        while len(vec) != 0:
            node = vec.pop()
            res.append(node.value)

            if node.right != None:
                vec.append(node.right)
            if node.left != None:
                vec.append(node.left)
        return res


root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(3)

root.left.left = TreeNode(4);root.left.right = TreeNode(5)
root.right.left = TreeNode(6);root.right.right = TreeNode(7)

s = Solution()
print(s.traversal(root))
