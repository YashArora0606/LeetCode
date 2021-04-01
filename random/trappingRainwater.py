class Solution:

    # Solution 1: Intuitive, O(n) time, O(n) space
    def trap(self, height: List[int]) -> int:
        
        # Create a corresponding array holding the largest value to its left
        tallest_left = 0
        tallest_lefts = []
        for value in height:
            tallest_lefts.append(tallest_left)
            tallest_left = max(tallest_left, value)
        
        # Create a corresponding array holding the largest value to its right
        tallest_right = 0
        tallest_rights = []
        for value in reversed(height):
            tallest_rights.insert(0, tallest_right)
            tallest_right = max(tallest_right, value)
        
        # Water at that index is the min of the tallest to the left and tallest
        # to the right, subtracting the height at that position
        total = 0
        for i in range(len(height)):
            water = min(tallest_rights[i], tallest_lefts[i]) - height[i]

            # If negative or 0, ignore water calculated at that position
            if water > 0:
                total += water

        return total
    
    # Solution 2: Optimized, O(n) time, O(n) space
    def trap(self, height: List[int]) -> int:
        tallest = 0
        tallests = []
        for value in height:
            tallests.append(tallest)
            tallest = max(tallest, value)
        total = 0
        tallest = 0
        for i in range(len(height) - 1, -1, -1):
            tallests[i] = min(tallests[i], tallest)
            tallest = max(tallest, height[i])
            water = tallests[i] - height[i]
            if water > 0:
                total += water

        return total