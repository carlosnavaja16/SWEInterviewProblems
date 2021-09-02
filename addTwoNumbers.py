"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the
sum as a linked list.

You may assume the two numbers do not contain any
leading zero, except the number 0 itself.

"""

class ListNode:
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        lAnswer = lDummy = ListNode(0)
        carry = 0

        while True:
            
            sum = 0
            
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            
            sum += carry
            carry = int(sum/10)
            lDummy.val = sum%10

            if l1!=None or l2!=None or carry != 0:
                lDummy.next = ListNode(0)
                lDummy = lDummy.next
            else: 
                break

        return lAnswer


