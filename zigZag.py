class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1): return s
        
        sLen = len(s)
        x = 0
        y = 0
        count = 0
        arr2d = [["" for i in range(sLen)] for j in range(numRows)]

        while count < sLen:
            
            #do while y cordinate is < numRows
            while y < numRows and count < sLen:
                arr2d[y][x] = s[count]
                y += 1
                count += 1

            y -= 2
            x += 1
            
            while y >= 0 and count < sLen:
                arr2d[y][x] = s[count]
                y -= 1
                x += 1
                count += 1
            
            y += 2
            x -= 1
        
        
        zigZag = ""
        for x in range(numRows):
            for y in range(sLen):
                if arr2d[x][y] != "":
                    zigZag += arr2d[x][y]
                    
        return zigZag
            
