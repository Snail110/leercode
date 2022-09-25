class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 比较两个树是否对称
class Solution:
    def compare(self,left:TreeNode,right:TreeNode):

        if left != None and right == None:
            return False
        elif left == None and right != None:
            return False
        elif left == None and right == None:
            return True
        elif left.value != right.value:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)

        return outside and inside

    def main(self,root:TreeNode):
        if root == None:
            return True
        return self.compare(root.left, root.right)

root = TreeNode(1);root.left = TreeNode(2);root.right = TreeNode(2)

# root.right.left = TreeNode(4);root.right.right = TreeNode(7)

s = Solution()

print(s.main(root))