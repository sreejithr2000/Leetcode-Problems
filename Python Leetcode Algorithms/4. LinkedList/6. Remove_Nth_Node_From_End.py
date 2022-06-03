# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def remove_n_from_end(self, head: ListNode, n):
        temp = head
        length = 0
        while temp:
            length +=1
            temp = temp.next
        pos = length - n

        temp = head

        if pos >= 1:
            for i in range(0, pos-1):
                temp = temp.next
            temp.next = temp.next.next
            
        else:
            head = head.next
        
        return head  # Remove this if you wanna see console o/p 
        
        while head:
            print(head.val)
            head = head.next
            

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

ans = s.remove_n_from_end(l1, 5)
print(ans)

# https://leetcode.com/problems/linked-list-cycle/
