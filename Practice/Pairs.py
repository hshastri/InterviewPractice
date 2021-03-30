def sockMerchant(n, ar):
    newArr = ar
    newArr.sort()
    frequencyDict = {}
    socks = set(ar)
    for sock in socks:
        frequencyDict[sock] = getFrequencyOfSock(newArr, sock)

    # print(frequencyDict)
    pairs = 0
    for sockFrequency in frequencyDict.values():
        pairs += (sockFrequency // 2)
    return pairs

def getFrequencyOfSock(ar, val):
    count = 0
    for element in ar:
        if element == val:
            count += 1
    return count
