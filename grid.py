memo = {}

def traverseGird(h,w):
    if (h,w) in memo:
        return memo[(h,w)]

    elif h == 1 and w == 1:
        return 1
    
    elif h == 0 or w == 0:
        return 0
    
    else:
        memo[(h,w)] = traverseGird(h - 1, w) + traverseGird(h, w - 1)
        return memo[(h,w)]

print(traverseGird(1,1))
print(traverseGird(3,3))
print(traverseGird(18,18))

