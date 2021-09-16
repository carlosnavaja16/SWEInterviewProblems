class Solution:
    def romanToInt(self, s: str) -> int:
        
        sLen = len(s)
        
        romanNums = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        
        num = 0
        
        for i in range(0,sLen):
            
            if i == sLen - 1:
                num += romanNums[s[i]]
                
            elif romanNums[s[i]] < romanNums[s[i+1]]:
                num -= romanNums[s[i]]
            else: 
                num += romanNums[s[i]]
            
        return num
