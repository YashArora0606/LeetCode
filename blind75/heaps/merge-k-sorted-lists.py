# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        arr = []
        heapq.heapify(arr)
        
        for node in lists:
            while node:
                heapq.heappush(arr, node.val)
                node = node.next
                
        if len(arr) == 0:
            return None
        
        node = ListNode(heapq.heappop(arr))
        head = node
        
        for i in range(len(arr)):
            node.next = ListNode(heapq.heappop(arr))
            node = node.next
        
        return head