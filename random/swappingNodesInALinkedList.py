# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        node = head
        
        for i in range(k - 1):
            node = node.next
            
        ahead = node
        
        behind = head
        
        while node.next != None:
            node = node.next
            behind = behind.next            

        ahead.val, behind.val = behind.val, ahead.val
        
        return head
