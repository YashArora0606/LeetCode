# Problem: Given a sorted list of integers, return a list of their squares, sorted.
# Example: [-7,-3,-1,4,8,12] --> [1, 9, 16, 49, 64, 144]
# Source: Facebook
def sortedSquaredArray(lst):
    left = 0
    right = len(lst) - 1q
    output = [None] * len(lst)
    for i in range(len(lst)-1, -1, -1):
        if abs(lst[left]) >= lst[right]:
            output[i] = lst[left] * lst[left]
            left += 1
        elif abs(lst[left]) < lst[right]:
            output[i] = lst[right] * lst[right]
            right -= 1
    return output
