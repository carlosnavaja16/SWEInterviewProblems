def oneReplacementAway(a: str, b: str) -> bool:
    differences = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1
    return differences <= 1

def oneInsertionAway(a: str, b: str) -> bool:
    differences = 0
    aPtr = 0
    bPtr = 0

    while bPtr < len(b):
        if aPtr == len(a):
            if differences <= 1:
                return True
            else:
                return False
        elif a[aPtr] == b[bPtr]:
            aPtr += 1
            bPtr += 1
        elif a[aPtr] != b[bPtr]:
            differences += 1
            bPtr += 1     

    return differences <= 1   

def oneAway(a: str, b: str) -> bool:
    if len(a) == len(b):
        return oneReplacementAway(a, b)
    elif len(a) - 1 == len(b):
        return oneInsertionAway(b, a)
    elif len(a) + 1 == len(b):
        return oneInsertionAway(a, b)
    else:
        return False
