def palindromePermutation(s: str) -> bool:
    hash = {}

    for char in s:
        if char == ' ': continue
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1
    
    odd = 0

    for v in hash.values():
        if v % 2 != 0:
            odd += 1
    
    return odd <= 1