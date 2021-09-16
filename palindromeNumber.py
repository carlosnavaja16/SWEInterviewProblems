class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        if x >= 0 and x <= 9: return True
        
        s = str(x)
        sLen = len(s)
        halfSLen = int(sLen/2)
        
        if sLen % 2 == 0:
            left = halfSLen - 1
            right = left + 1
        else:
            left = halfSLen - 1
            right = left + 2
            
        while left >= 0:
            if s[left] != s[right]: return False
            left -= 1
            right += 1
        
        return True
