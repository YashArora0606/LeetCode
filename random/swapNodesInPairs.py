# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Swapping Values
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        node = head
        
        while node.next != None:
            first = node.val
            node.val = node.next.val
            node = node.next
            node.val = first
            if node.next != None:
                node = node.next
            
        return head

# Swapping Pointers
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        node = head
        
        first_swap_complete = False
        prev = None
        
        while node.next != None:
            
            second = node.next

            if prev != None:
                prev.next = node.next
            
            node.next = node.next.next
            second.next = node
            
            if not first_swap_complete:
                head = second
                first_swap_complete = True

            prev = node
            
            if node.next != None:
                node = node.next
            
        return head