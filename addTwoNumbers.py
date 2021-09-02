"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the
sum as a linked list.

You may assume the two numbers do not contain any
leading zero, except the number 0 itself.

"""


#Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1 = []
        list2 = []
        
        while True:
            list1.append(l1.val)
            if(l1.next):
                l1 = l1.next
            else:
                break
        
        while True:
            list2.append(l2.val)
            if(l2.next):
                l2 = l2.next
            else:
                break
        
        num1 = 0
        num2 = 0
        
        for index, value in enumerate(list1):
            num1 += value*(10**index)
            
        for index, value in enumerate(list2):
            num2 += value*(10**index)
            
        print(num1)
        print(num2)
        
        numAnswer = str(num1+num2)
        
        lAnswer = ListNode()
        lPointer = ref(lAnswer)
        
        for n in range(len(numAnswer)-1, -1,-1):
            print(int(numAnswer[n]))
            lPointer.value = int(numAnswer[n])
            lPointer.next = ListNode()
            lPointer = lPointer.next     
        
        return lAnswer