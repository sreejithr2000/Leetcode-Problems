class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_num(self, List1: ListNode, List2:ListNode) -> ListNode:
        #head1 and head2 contain 1st node of the whole list : basically HEAD only
        head1 = List1
        head2 = List2 

        if head1 == None and head2 == None:
            return None
            
        dummy = head3 = ListNode # creating instance of above class to store values

        carry = 0
        count1 = 0
        count2 = 0
        temp_count1 = List1
        temp_count2 = List2

        while temp_count1.next is not None:
            count1 += 1
            temp_count1 = temp_count1.next

        while temp_count2.next is not None:
            count2 += 1
            temp_count2 = temp_count2.next
        
        if(count1 > count2):
            for i in range(0, count1 - count2):
                new_node= ListNode(0)
                temp_count2.next = new_node
                temp_count2 = temp_count2.next
        
        if(count1 < count2):
            for i in range(0, count2 - count1):
                new_node= ListNode(0)
                temp_count1.next = new_node
                temp_count1 = temp_count1.next         #Till here: Adding zeros to the list to match up the length of two lists
        
        while head1 is not None and head2 is not None:
            # print(head1.val + head2.val)
            if carry + head1.val + head2.val >= 10:
                if carry + (head1.val + head2.val)%10 == 10:
                    head3.next = ListNode(0)
                    carry = 1
                else:
                    head3.next = ListNode(carry + (head1.val + head2.val)%10)
                    carry = int((head1.val + head2.val)/10)
            else:
                head3.next = ListNode(carry + head1.val + head2.val)
                carry = 0

            head1 = head1.next
            head2 = head2.next
            head3 = head3.next                           # Till here: Adding sum to dummy list by handling carry over
            
        last_val1 = 0
        temp1 = List1
        temp2 = List2
        while temp1.next:
            temp1 = temp1.next
        last_val1 = temp1.val
        
        last_val2 = 0
        while temp2.next:
            temp2 = temp2.next
        last_val2 = temp2.val
            
        if carry + last_val1 + last_val2 >= 10 :
            carry_node = ListNode(carry)
            head3.next = carry_node                       # Till here: if sum of last element from 2 list is >= 10, add carry overs

        return dummy.next
    
s = Solution()
l1_1 = ListNode(8)
l1_2 = ListNode(3)
l1_3 = ListNode(2)
# l1_4 = ListNode(9)
# l1_5 = ListNode(9)
# l1_6 = ListNode(9)
# l1_7 = ListNode(9)

l1_1.next = l1_2
l1_2.next = l1_3
# l1_3.next = l1_4
# l1_4.next = l1_5
# l1_5.next = l1_6
# l1_6.next = l1_7

# l1: 2->4->3->3

l2_1 = ListNode(9)
l2_2 = ListNode(2)
l2_3 = ListNode(1)
# l2_4 = ListNode(9)

l2_1.next = l2_2
l2_2.next = l2_3
# l2_3.next = l2_4

# l2: 5->6->4

ans = s.add_two_num(l1_1, l2_1)
# print(ans)

while ans != None:
    print(ans.val)
    ans = ans.next


# https://leetcode.com/problems/add-two-numbers/