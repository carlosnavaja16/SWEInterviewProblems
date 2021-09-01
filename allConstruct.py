"""
Write a function allConstruct(target, wordBank)
that accepts a target string and an array of strings.

the function should return a 2d array with the different 
combinations that add up to target

you may reuse elements of the wordbank as many times
as needed.
"""


memo = {}


def allConstruct(target, wordBank):
    if target in memo: return memo[target]
    if target == "": return [[]]

    combination = []

    for word in wordBank:
        if target.__contains__(word): 
            if target.index(word) == 0:
                newTarget = target.removeprefix(word)
                result = allConstruct(newTarget, wordBank)
                for r in result:
                    r.insert(0,word)
                    combination.append(r)

    memo[target] = combination;                
    return combination

print(allConstruct("purple",["purp", "p","ur", "le", "purpl"]))
print(allConstruct("abcdef",["ab", "abc","cd", "def", "abcd"])) 
print(allConstruct("skateboard",["bo", "rd", "ate", "t", "ska","sk", "boar"])) 
#print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeeeeee"])) #0

