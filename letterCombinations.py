class Solution:
    
    letters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: return []
        if len(digits) == 1: return self.letters[digits]
        
        letterCombos = self.letterCombinations(digits[1:])
        
        newCombos = []
        
        for l in self.letters[digits[0]]:    
            for c in letterCombos:
                newCombos.append(l + c)
                
        return newCombos
        
        
