class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        if digits == "":
            return res
        
        for letter in num_to_letters[digits[0]]:
            res.append(letter)
            
        if len(digits) == 1:
            return res
        
        for i in range(1, len(digits)):
            new_res = []
            for elem in res:
                for letter in num_to_letters[digits[i]]:
                    new_res.append(elem + letter)
            res = new_res
        
        return res

                