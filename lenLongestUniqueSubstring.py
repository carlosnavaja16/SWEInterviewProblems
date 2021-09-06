class Solution:
    def addToCharMap(self, m, c):
        if c in m:
            m[c] += 1
        else:
            m[c] = 1
    
    def removeFromCharMap(self, m, c):
        if c in m:
            if m[c] == 1:
                m.pop(c)
            else:
                m[c] -= 1
            
            
    def allUniqueInMap(self, m):
        allUnique = True
        for c in m:
            if m[c] > 1:
                allUnique = False
        return allUnique

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sLen = len(s)
        windowStart = 0
        longestSubstring = 0
        charMap = {}

        for windowEnd in range(sLen):
            self.addToCharMap(charMap, s[windowEnd])
            
            if self.allUniqueInMap(charMap):
                longestSubstring = max(longestSubstring, windowEnd-windowStart + 1)
                
            else:    
                while not self.allUniqueInMap(charMap):
                    self.removeFromCharMap(charMap, s[windowStart])
                    windowStart += 1
        
        return longestSubstring