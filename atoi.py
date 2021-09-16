class Solution:
    
    def strToInt(self, s: str, negative: bool) -> int:
        
        if s == "": return 0 
               
        x = int(s)
        
        if negative: x *= -1
            
        if x >= 2**31 - 1: return 2**31 -1
        if x <= -2**31: return -2**31

        return x
    
    def myAtoi(self, s: str) -> int:
        
        if s == "" or s == " ": return 0
        
        count = 0
        sLen = len(s)
        intStr = ""
        negative = False
        
        if s[count] == " ":
            while count < sLen and s[count] == " ":
                count += 1
        
        if count < sLen and (s[count].isdigit() or s[count] == "+" or s[count] == "-"):
            if s[count] == "-":
                negative = True
                count += 1
            elif s[count] == "+":
                count += 1
            while count < sLen and s[count].isdigit():
                intStr += s[count]
                count += 1

        return self.strToInt(intStr, negative)
