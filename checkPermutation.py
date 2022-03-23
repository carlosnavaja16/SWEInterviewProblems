def checkPermutation(a: str, b: str) -> bool:
    hash = {}

    for char in b:
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1

    for char in a:
        if char not in hash or hash[char] == 0:
            return False
        else:
            hash[char] -= 1
            
    return True