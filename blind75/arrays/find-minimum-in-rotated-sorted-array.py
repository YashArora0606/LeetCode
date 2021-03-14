class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Important: Fundamentals of binary search
        bot = 0
        top = len(nums) - 1
            
        while bot < top:
            mid = (top + bot) // 2
            if nums[mid] > nums[top]:
                bot = mid + 1
            else:
                top = mid

        return nums[bot]
        