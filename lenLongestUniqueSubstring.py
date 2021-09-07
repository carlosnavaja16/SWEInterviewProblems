class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = len(s)
        windowStart = longestSubstring = 0
        charMap = {}
        for windowEnd in range(sLen):     
            if s[windowEnd] not in charMap: charMap[s[windowEnd]] = 1
            else: charMap[s[windowEnd]] += 1        
            while charMap[s[windowEnd]] > 1:
                charMap[s[windowStart]] -= 1
                windowStart += 1                
            longestSubstring = max(longestSubstring, windowEnd-windowStart + 1)
        return longestSubstring
            
        