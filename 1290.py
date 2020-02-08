# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        temp = head
        n = 0
        while(temp != None):
            n += 1
            temp = temp.next
        power = 2**(n-1)
        temp = head
        total = 0
        while(temp != None):
            if temp.val == 1:
                total += power
            power /= 2
            temp = temp.next
        return total
