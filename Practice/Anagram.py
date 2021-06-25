def findAnagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return 0
    else:
        frequncyDict1 = getFreqencyDict(str1)
        print(frequncyDict1)
        frequncyDict2 = getFreqencyDict(str2)
        print(frequncyDict2)

    arr = getDeltaArr(frequncyDict1, frequncyDict2)
    # print(arr)
    return sum(arr)

def getDeltaArr(dict1, dict2):
    arrOfVals = []
    keysA = dict1.keys()
    keysB = dict2.keys()
    setA = set(keysA)
    setB = set(keysB)
    commonElements = setA.intersection(setB)
    for char in dict1:
        if char not in commonElements:
            arrOfVals.append(dict1[char])
        elif char in commonElements:
            arrOfVals.append(abs(dict1[char] - dict2[char]))  # only need to do it once for the common elements
    for char in dict2:
        if char not in commonElements:
            arrOfVals.append(dict2[char])
    return arrOfVals

def getFreqencyDict(str):
    dict = {}
    for char in str:
        count = 1
        if char not in dict:
            dict[char] = count
        elif char in dict:
            dict[char] += 1
    return dict
