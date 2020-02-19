class Solution(object):
    def numUniqueEmails(self, emails):
        unique_addresses = {}
        for email in emails:
            name = email.split("@")[0]
            domain = email.split("@")[1]
            name = name.split("+")[0]
            name = name.replace(".","")
            full_address = name + "@" + domain
            if full_address not in unique_addresses:
                unique_addresses[full_address] = 1
        return len(unique_addresses.keys())
        """
        :type emails: List[str]
        :rtype: int
        """
