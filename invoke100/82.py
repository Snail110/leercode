class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Solution:
    def main(self,head):
        jummy = ListNode(-1)
        jummy.next = head
        cur = jummy
        # 保证下一位，下下一位都有
        while cur.next and cur.next.next:
            # 判断下一位，下下一位是否相等，如果相等 记录x值
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
               # 去重复=将cur下一个指针指向下下一个就达到了
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return jummy.next

head = ListNode(0)
cur = head
for i in [1,2,2,3,4,4,5]:
    cur.next = ListNode(i)
    cur = cur.next

s = Solution()
res = s.main(head)

while res:
    print(res.val)
    res = res.next
            
            
            
            

