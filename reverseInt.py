class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        
        if x < 0: negative = True
            
        xStr = str(abs(x)) 
        xStr = xStr[::-1]
        x = int(xStr)
        
        if negative: x *= -1
        if x > 2**31 or x < -2**31: return 0 

        return x
