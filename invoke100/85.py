class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Solution:
    def main(self,head,x):
        small = ListNode(0)
        smallHead = small
        large = ListNode(0)
        largeHead = large
        while head:
            if head.val <=x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        large.next = None
        small.next = largeHead.next
        return smallHead.next

head = ListNode(0)
cur = head
for i in [1,2,2,3,4,4,5]:
    cur.next = ListNode(i)
    cur = cur.next

# while head:
#     print(head.val)
#     head = head.next

s = Solution()
res = s.main(head,3)

while res:
    print(res.val)
    res = res.next