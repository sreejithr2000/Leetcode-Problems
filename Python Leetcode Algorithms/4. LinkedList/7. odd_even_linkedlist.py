# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def odd_even(self, head: ListNode):
        odd_head = odd = head
        even_head = even = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head

        return odd_head # Remove this if you wanna see console o/p 
        
        while odd_head:
            print(odd_head.val)
            odd_head = odd_head.next


s = Solution()
l1 = ListNode(2)
l2 = ListNode(5)
l3 = ListNode(4)
l4 = ListNode(1)
l5 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

ans = s.odd_even(l1)
print(ans)

# https://leetcode.com/problems/odd-even-linked-list/
