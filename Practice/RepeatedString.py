def repeatedString(s, n):
    L = len(s)
    return s.count('a') * (n // L) + s[:n % L].count('a')

"""def repeatedString(s, n):
    tempStr = stringBuilder(s, n)
    count = 0
    for char in tempStr:
        if char == 'a':
            count += 1
    return count

def stringBuilder(s, n):
    tempStr = ""
    currentStrLength = len(tempStr)

    while currentStrLength <= n:
        tempStr += s
        currentStrLength += len(s)
        if currentStrLength > n:
            tempStr = tempStr[:n]
    return tempStr"""