class ListNode:
   def __init__(self,val=0):
      self.val = val
      self.next = None
      
class Solution:
    def main(self,head,left,right):
        # 首先创建虚拟节点
        jummy = ListNode(-1)
        jummy.next = head
        pre = jummy
        for i in range(left-1):
            pre = pre.next
        
        cur = pre.next # 当前反转的节点
        for j in range(right-left):
            next = cur.next # 赋值下一个节点
            cur.next = next.next # 尾部链接
            next.next = pre.next # 中部反转
            pre.next = next # 头部链接
        return jummy.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s = Solution()
res = s.main(head,2,4)
while res:
    print(res.val)
    res = res.next
        

        
        



