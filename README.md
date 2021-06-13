# CSCI-UA2-NYUSHANGHAI

Intended To Be Full Of Bugs For Not Being Copied.

Past Assignments Solutions For The Course.

Finally Got a A on this course
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    current = dummy = ListNode()
    carry, value = 0, 0
    while carry or l1 or l2:
        value = carry
        if l1: l1, value = l1.next, l1.val + value
        if l2: l2, value = l2.next, l2.val + value
        carry, value = divmod(value, 10)
        current.next = ListNode(value)
        current = current.next
        return dummy.next
        
