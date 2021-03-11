class Solution(object):
    def isPalindrome(self, x):
        if x < 0: # Numbers less than 0 will never be palindromes
            return False
        d = 1
        n = x
        while n/10 != 0: # Determine d, the number of digits
            n = n/10
            d += 1
        for i in range((d/2)+1): # Only need to go between 1 more than half the number
            if x/(10**i)%10 != x/(10**(d-i-1))%10: # If digit on left is not corresponding digit on right, exit
                return False
        return True # If everything passes it is a palindrome
