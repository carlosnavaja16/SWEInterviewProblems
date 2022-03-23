def URLify(string: str) -> str:
    string = list(string)
    print(string)
    end = len(string) - 1
    charPtr = 0
    
    for i in range(len(string) - 1, -1 ,-1):
        if string[i] != ' ':
            print(f'charPtr = {i}')
            charPtr = i
            break
    
    for i in range(charPtr, -1, -1):
        if string[i] == ' ':
            string[end] = '0'
            string[end - 1] = '2'
            string[end - 2] = '%'
            end -= 3
        else:
            string[end] = string[i]
            end -= 1

    return ''.join(string)