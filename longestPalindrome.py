class Solution:
    
    lowerBound = 0
    maxLen = 0
    
    def expandPalindrome(self, s: str, sLen: int,j: int, k: int):
        currLen = 0
        while j >= 0 and k < sLen and s[j] == s[k]:
            currLen = k - j + 1
            if currLen > self.maxLen:
                self.lowerBound = j
                self.maxLen = currLen
            j -= 1
            k += 1
        
    
    def longestPalindrome(self, s: str) -> str:
        
        sLen = len(s)
        if sLen < 2:
            return s
        
        for i in range(1, sLen):
            self.expandPalindrome(s,sLen,i,i)
            self.expandPalindrome(s,sLen,i,i-1)
        
        return s[self.lowerBound:self.lowerBound + self.maxLen]
    
