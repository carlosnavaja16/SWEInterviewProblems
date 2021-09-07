class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        listLen = len(releaseTimes)
        longestDuration = releaseTimes[0]
        slowestKey = keysPressed[0]
        
        for n in range(1,listLen):
            if releaseTimes[n]-releaseTimes[n-1] == longestDuration:
                if slowestKey < keysPressed[n]:
                    slowestKey = keysPressed[n]
            elif releaseTimes[n]-releaseTimes[n-1] > longestDuration:
                slowestKey = keysPressed[n]
                longestDuration = releaseTimes[n]-releaseTimes[n-1]
        
        return slowestKey