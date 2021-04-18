class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        bot = 0
        top = len(nums) - 1
        
        # The <= is needed because it needs one last iteration when they are equal
        while bot <= top:
            mid = (bot + top) // 2
            
            if nums[mid] == target:
                return mid
            
            # Left side is sorted, so breakpoint is at right side
            elif nums[mid] >= nums[bot]:
                
                if target < nums[mid] and target >= nums[bot]:
                    top = mid - 1
                else:
                    bot = mid + 1
            
            # Left side is not sorted, so breakpoint is at left side
            else:
                
                if target > nums[mid] and target <= nums[top]:
                    bot = mid + 1
                else:
                    top = mid - 1
                    
        return -1
        