# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        head = tail
        carry = False
        while l1 and l2:
            sum = l1.val + l2.val
            if carry == True:
                sum +=1
                carry = False
            if sum > 9:
                carry = True
                sum = sum%10
            tail.next = ListNode(sum)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        return head.next
