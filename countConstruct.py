"""
Write a function countConstruct(target, wordBank)
that accepts a target string and an array of strings.

the function should return the number of ways a
the target can be constructed by concatinating elements
of the wordBank array

you may reuse elements of the wordbank as many times
as needed.
"""

memo = {}

def countConstruct(target: str, wordBank: list[str]) -> int:
    count = 0
    if target == "": return 1
    if target in memo: return memo[target]

    for word in wordBank:
        if target.__contains__(word):
            if target.index(word) == 0:
                newTarget = target.removeprefix(word)
                count += countConstruct(newTarget, wordBank)
    memo[target] = count
    return count


print(countConstruct("purple",["purp", "p","ur", "le", "purpl"])) #2
print(countConstruct("abcdef",["ab", "abc","cd", "def", "abcd"])) #1
print(countConstruct("skateboard",["bo", "rd", "ate", "t", "ska","sk", "boar"])) #0
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeeeeee"])) #0

