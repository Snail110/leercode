class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    # 组成环形
    def main(self,head:ListNode,k):
        if not head or k==0:
            return head
        cur = head
        ll = 1
        # 计算长度
        while cur.next:
            cur = cur.next
            ll += 1

        # 移动步数
        add = ll - k % ll
        if add == ll:
            return head
        # 链接环
        cur.next = head
        # 移动 add步
        while add >0:
            cur = cur.next
            add -= 1
        
        ret = cur.next # 赋新值
        cur.next = None # 断开
        return ret
    # 快慢指针
    def main1(self,head:ListNode,k):
        if not head or k == 0:
            return head
        
        cur = head
        ll = 1
        # 统计链表长度，不迭代到最后
        while cur.next:
            cur = cur.next
            ll += 1
        slow = head
        quick = head
        n = k % ll
        while n>0:
            quick = quick.next
            n -= 1
        while quick.next:
            quick = quick.next
            slow = slow.next
        cur.next = head
        head = slow.next
        slow.next = None
        return head

s = Solution()
head = ListNode(0)
cur = head
for i in range(1,5):
    cur.next = ListNode(i)
    cur = cur.next
h = s.main1(head,2)
while h:
    print(h.val)
    h = h.next

# print(s.main1(head,2))