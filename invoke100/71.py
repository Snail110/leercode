class Solution:
    def main(self,path):
        stack = []
        path = path.split('/')
        ll = len(path)
        for i in range(ll):
            if path[i] == '':
                continue
            elif path[i] == '.':
                continue
            elif path[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[i])
        
        stack = '/' + '/'.join(stack)
        return stack

s = Solution()
path = "/../"
path = "/.../a/../b/c/../d/.//"
print(s.main(path))
