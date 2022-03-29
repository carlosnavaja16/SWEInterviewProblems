def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None: return head
        
    slow = head
    fast = head.next
    
    while fast:
        if fast.val == slow.val:
            fast = fast.next
            slow.next = fast
        else:
            slow = fast
            fast = fast.next
    
    return head              