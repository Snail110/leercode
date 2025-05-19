class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def main(self,p,q):
        
        def dfs(p,q):
            if p is None and q is None:
                return True
            if p is None or q is not None:
                return False
            if p.val != q.val:
                return False
            
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        return dfs(p,q)
    
s = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(5)
print(s.main(p,q))