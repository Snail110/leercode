class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Solution:
    def main(self,head):
        jummy = ListNode(-1)
        jummy.next = head
        cur = jummy
        while cur and cur.next:
            if cur.val == cur.next.val:
               x = cur.val
               # 如果cur.next=x，那么就用下下一个代替，进行下一步判断
               while cur.next and cur.next.val == x:
                   # 去重复=将cur下一个指针指向下下一个就达到了
                   cur.next = cur.next.next
            else:
                cur = cur.next
        return jummy.next
    
    def main1(self,head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                # 去重复=将cur下一个指针指向下下一个就达到了
                cur.next = cur.next.next
            else:
                # 迭代是将下一个指针指向当前
                cur = cur.next
        return head

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