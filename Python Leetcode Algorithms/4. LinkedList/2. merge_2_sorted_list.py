class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, List1: ListNode, List2:ListNode) -> ListNode:
        #head1 and head2 contain 1st node of the whole list : basically HEAD only
        head1 = List1
        head2 = List2 

        if head1 == None and head2 == None:
            return None
            
        head3 = dummy = ListNode # creating instance of above class to store values

        while head1 is not None and head2 is not None:
            if head1.val < head2.val: #comparing values from each list
                head3.next = head1 # storing small value to dummy list
                head1 = head1.next # i++ for small number
                head3 = head3.next # increment head3 pointer in dummy
            else:
                head3.next = head2
                head2 = head2.next
                head3 = head3.next
        
        while head1 is not None:
            head3.next = head1
            head1 = head1.next
            head3 = head3.next
        while head2 is not None:
            head3.next = head2
            head2 = head2.next
            head3 = head3.next
            
        return dummy.next
    
s = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)

l1_1.next = l1_2
l1_2.next = l1_4

# l1: 1->2->4

l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)

l2_1.next = l2_3
l2_3.next = l2_4

# l2: 1->3->4

ans = s.mergeTwoLists(l1_1, l2_1)
# print(ans)

while ans != None:
    print(ans.val)
    ans = ans.next


# https://leetcode.com/problems/merge-two-sorted-lists/