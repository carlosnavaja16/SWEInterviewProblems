def isUnique(string: str) -> bool:
    hashSet = set()
    for s in string:
        if s in hashSet:
            return False
        else:
            hashSet.add(s)
    return True

print(isUnique('asbcdefg'))
print(isUnique('abcdefe'))