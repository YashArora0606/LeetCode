class Solution(object):
    def defangIPaddr(self, address):
        defanged = ""
        for c in address:
            if c == '.':
                defanged += "[.]"
            else:
                defanged += c
        return defanged
        """
        :type address: str
        :rtype: str
        """
        
