class Solution:
    def main(self,a,b):
        ans = []
        a_list = list(a)
        b_list = list(b)
        if len(a_list) < len(b_list):
            tmp = a_list
            a_list = tmp
            b_list = tmp
        
        pre = 0
        while a_list and b_list:
            a1 = a_list.pop()
            b1 = b_list.pop()
            c = int(a1) + int(b1) + pre
            if  c <2:
                pre = 0
            elif c == 2:
                c = 0
                pre = 1
            elif c == 3:
                c = 1
                pre = 1
            ans.append(str(c))
        while a_list:
            a1 = a_list.pop()
            c = int(a1) + pre
            if  c <2:
                pre = 0
            elif c == 2:
                c = 0
                pre = 1
            elif c == 3:
                c = 1
                pre = 1
            ans.append(str(c))
        if pre == 1:
            ans.append(str(pre))
        ans = ans[::-1]
        return ''.join(ans)
    def main1(self,a,b):
        ans = []
        pre = 0
        a = list(a)
        b = list(b)
        a = a[::-1]
        b = b[::-1]
        n = max(len(a),len(b))
        for i in range(n):
            a1 = a[i] if i < len(a) else '0'
            b1 = b[i] if i < len(b) else '0'
            c = int(a1) + int(b1) + pre
            c = c % 2
            pre = c // 2
            ans.append(str(c))
        if pre == 1:
            ans.append(str(pre))
        ans = ans[::-1]
        return ''.join(ans)
            
s = Solution()
a = '1010'
b = '101'
print(s.main(a,b))
print(s.main1(a,b))
