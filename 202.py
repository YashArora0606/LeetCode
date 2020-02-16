class Solution(object):
    def isHappy(self, n):
        seen_nums = {}
        while(n != 1):
            if n in seen_nums:
                return False
            seen_nums[n] = 1
            digs = []
            while(n != 0):
                digs.append(n%10)
                n /= 10
            for dig in digs:
                n += dig*dig
        return True

        """
        :type n: int
        :rtype: bool
        """

        
