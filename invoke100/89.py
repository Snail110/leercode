class Solution:
    def main(self,n):
        res,head = [0],1
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(head + res[j])
            head <<= 1
        return res

s = Solution()
print(s.main(3))