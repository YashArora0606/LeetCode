# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 1. Calculate length of list
        temp = head
        l = 0
        while temp != None:
            l += 1
            temp = temp.next

        # 2. Find node at middle
        temp = head
        for i in range(l // 2 - 1):
            temp = temp.next
        right_head = temp.next

        # 3. Break connection between middle nodes
        temp.next = None

        # 4. Reverse right side of list
        temp = right_head
        prev = None
        while temp:
            ahead = temp.next
            temp.next = prev
            prev = temp
            temp = ahead

        # 5. Hold reference to right and left heads
        right_head = prev
        left_head = head

        # 6. Ensure all values of right and left side are the same
        for i in range(l // 2):
            if right_head.val != left_head.val:
                return False
            right_head = right_head.next
            left_head = left_head.next
        return True
