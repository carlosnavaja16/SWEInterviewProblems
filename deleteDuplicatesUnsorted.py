def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
    if not head or not head.next: return head
    
    slow = None
    fast = head
    present = set()
    dups = set()
    
    while fast:
        if fast.val in present:
            dups.add(fast.val)
        else:
            present.add(fast.val)
        slow = fast
        fast = fast.next
        
    print(dups)
        
    while head and head.val in dups:
        head = head.next

    if not head: return head
                
    slow = head
    fast = head.next 
    
    while fast:
        if fast.val in dups:
            slow.next = fast.next
            fast = fast.next
        else:
            slow = fast
            fast = fast.next

    return head