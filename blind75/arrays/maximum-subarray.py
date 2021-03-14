# This is referred to as kadanes algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        latest_max = float('-inf')
        overall_max = float('-inf')

        for num in nums:
            latest_max = max(latest_max + num, num) 
            overall_max = max(latest_max, overall_max)
        
        return overall_max