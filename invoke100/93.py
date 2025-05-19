class Solution:
    def main(self,s):
        ans = []
        path = []
        ll = len(s)
        def dfs(path,string):
            if len(path[::]) == 4:
                if len(''.join(path[::])) == ll:
                    ans.append('.'.join(path[::]))
                    return
                else:
                    return
            for i in [1,2,3]:
                if len(string) < i:
                    continue
                if int(string[:i]) > 255:
                    continue
                if len(string[:i])>1 and string[:i][0] == '0':
                    continue
                # if str(int(string[:i])) != string[:i]:
                #     continue
                path.append(string[:i])
                dfs(path,string[i:])
                path.pop()
        
        dfs(path,s)
        return ans
s = Solution()
string = '25525511135'
string = '0000'
string = '101'
print(s.main(string))
