class Solution:

    def intToRoman(self, num: int) -> str:
        romanNums = {  
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }
        
        romanStr = ""
        
        for i in romanNums:
            if num < i:
                continue
            else:
                romanStr += (num // i) * romanNums[i]
                num = num % i
            
        return romanStr
            
