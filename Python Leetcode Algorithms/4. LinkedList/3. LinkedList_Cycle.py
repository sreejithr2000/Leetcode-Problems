# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        arr = []
        while head is not None:
            arr.append(head.val)
        print(arr)
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l2

ans = s.hasCycle(l1)
print(ans)

# https://leetcode.com/problems/linked-list-cycle/
