class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        latest_max = nums[0]
        overall_max = nums[0]
        latest_min = nums[0]
        overall_min = nums[0]

        for i in range(1, len(nums)):
            
            num = nums[i]
            
            old_latest_max = latest_max
            latest_max = max(latest_max * num, latest_min * num, num) 
            latest_min = min(old_latest_max * num, latest_min * num, num) 

            overall_min = min(latest_min, overall_min)            
            overall_max = max(latest_max, overall_max)
        
        return overall_max