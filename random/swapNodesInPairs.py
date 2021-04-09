# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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