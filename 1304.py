class Solution(object):
    def sumZero(self, n):
        nums = []
        for i in range(-1*(n/2), n%2, 1):
            nums.append(i)
        for i in range(1, n/2+1, 1):
            nums.append(i)
        return nums
        """
        :type n: int
        :rtype: List[int]
        """
        
