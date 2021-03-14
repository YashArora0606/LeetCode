class Solution:
    def maxArea(self, height: List[int]) -> int:
  
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            
            current_area = (right - left) * min(height[left], height[right])
            
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
