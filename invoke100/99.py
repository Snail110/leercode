class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def main(self,root):
        # 中序遍历
        path = []
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            path.append(root)
            dfs(root.right)
        
        dfs(root)
        pre = path[0]
        x = None
        y = None
        for i in range(1,len(path)):
            if pre.val > path[i].val:
                y = path[i]
                if not x:
                    x = pre
                
            pre = path[i]
        if x and y:
            x.val,y.val = y.val,x.val
        return root
s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

print(s.main(root))