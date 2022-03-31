def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    if not head: return head
    if not head.next: return head.next
    
    slow = ListNode(next=head)
    fast = head
    
    while fast.next:
        fast = fast.next
        if fast.next:
            fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return head
