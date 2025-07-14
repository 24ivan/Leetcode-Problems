# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode("This will start as the beginning of the list and should not be in the output")
        head = tail
        carry = False
        while l1 or l2 or carry:
            l1pointer = l1.val if l1 else 0 #if l1 is null, don't add anything from l1
            l2pointer = l2.val if l2 else 0 #save as above for l2
            sum = l1pointer + l2pointer
            if carry == True: #If there was a carry bit from the previous iteration, add it to the sum
                sum +=1
                carry = False
            if sum > 9: #If sum is 10 or more, save a carry bit for the next iteration
                carry = True
            tail.next = ListNode(sum%10) #Only put the right most digit in the current node
            tail = tail.next
            l1 = l1.next if l1 else None #if l1 node is null, have l1 remain as null for rest of loop
            l2 = l2.next if l2 else None #same as above for l2
        return head.next
