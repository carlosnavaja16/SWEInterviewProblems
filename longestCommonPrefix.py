class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strsLen = len(strs)
        if strsLen == 1:
            return strs[0]
        
        shortestWord = strs[0]
        
        for s in range(1,strsLen):
            if len(strs[s]) < len(shortestWord):
                shortestWord = strs[s]
                
        print("shortest word is " + shortestWord)
        
        i = 0
        longestPrefix = ""
    
        for i in range(len(shortestWord)):
            for k in range(strsLen):
                if shortestWord[i] != strs[k][i]:
                    return longestPrefix 
            longestPrefix += shortestWord[i]
        
        return longestPrefix
            
