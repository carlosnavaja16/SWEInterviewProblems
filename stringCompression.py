def stringCompression(string: str) -> str:

    string = list(string)
    
    result = []
    currentLetter = string[0]
    counter = 0

    for i in range(len(string)):
        if string[i] == currentLetter:
            counter += 1
        else:
            result.append(currentLetter)
            result.append(str(counter))
            currentLetter = string[i]
            counter = 1
    
    result.append(currentLetter)
    result.append(str(counter))

    if len(result) >= len(string):
        return ''.join(string)
    else:
        return ''.join(result)