class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToValue = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        subSymbolToValue = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        total = 0
        while len(s) > 0:
            if len(s) > 1:
                comb = str(s[0]) + str(s[1])
                if comb in subSymbolToValue:
                    total += subSymbolToValue[comb]
                    s = s[2:]
                    continue
            total += symbolToValue[s[0]]
            s = s[1:]
        return total
                    

                    
            