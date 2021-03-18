class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob_house = 0
        skip_house = 0
        
        old_rob_house = 0
        old_skip_house = 0
        
        for num in nums:

            rob_house = old_skip_house + num
            
            skip_house = max(old_rob_house, old_skip_house)
            
            old_rob_house = rob_house
            old_skip_house = skip_house
            
        return max(rob_house, skip_house)