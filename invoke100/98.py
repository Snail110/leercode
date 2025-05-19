class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def main(self,root):
        def dfs(root:TreeNode, low, high):
            if root is None:
                return True
            # 判断 是否符合二叉嗖嗖树
            if not (low < root.val < high):
                return False
            # 左 最大值为节点
            l = dfs(root.left, low, root.val)
            # 右，最小智为 节点
            r = dfs(root.right, root.val,high)
            return l and r
        
        min_num = -2**23
        max_num = 2**23
        return dfs(root,min_num,max_num)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
print(s.main(root))