memo = {}

def canConstruct(target: str, wordBank: list[str]) -> bool:
    if target in memo: return memo[target]
    if target == '': return True
         
    for word in wordBank:
        if target.__contains__(word):
            if target.index(word) == 0:
                newTarget = target.removeprefix(word)
                print("target is now: " + newTarget)
                if canConstruct(newTarget,wordBank) == True:
                    memo[newTarget] = True
                    return True
    
    memo[target] = False
    return False
    
    

print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeeeeee"]))

""""
target = "abcdef"

word = "zzz"

print(target.index(word))
print(target.removeprefix(word))

target.__contains__()
"""