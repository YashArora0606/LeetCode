# My original solution thought out logically
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        
        product_left = 1
        product_right = 1
        
        for i in range(1, len(nums)):
            
            product_left *= nums[i - 1]
            left.append(product_left)
            
            product_right *= nums[len(nums) - i]
            right.append(product_right)
        
        products = []
        
        for i in range(len(nums)):
            products.append(left[i] * right[len(nums) - i - 1])
        
        return products

# Optimized version using O(1) space (return array not counted) and O(n) time
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        
        product_left = 1
        product_right = 1
        
        for i in range(1, len(nums)):
            
            product_left *= nums[i - 1]
            products[i] *= product_left
            
            product_right *= nums[len(nums) - i]
            products[len(nums) - i - 1] *= product_right
        
        return products
        
        