# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        prev= None
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return prev

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4

ans = s.reverseList(l1)

while ans != None:
    print(ans.val)
    ans = ans.next

# print(ans)
        
        
        