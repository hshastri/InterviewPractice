def checkMagazine(magazine, note):
    setMagazine = getSetOf(magazine)
    setNote = getSetOf(note)
    """print(setMagazine)
    print(setNote)"""
    wordsInMagazine = getArrOfWords(magazine)
    wordsInNote = getArrOfWords(note)
    frequencyMagazine = getFreqencyDict(wordsInMagazine)
    frequencyNote = getFreqencyDict(wordsInNote)
    commonElements = setMagazine.intersection(setNote)
    """print(frequencyMagazine)
    print(frequencyNote)"""
    # print(intersectionOfArrays(wordsInMagazine, wordsInNote))

    if commonElements != setNote:
        print("No")
        return
    else:
        hasWords = True
        for words in commonElements:
            if frequencyMagazine[words] != frequencyNote[words]:
                hasWords = False
        if hasWords:
            print("Yes")
        else:
            print("No")

"""def intersectionOfArrays(arr1, arr2):
    commonElements = []
    if len(arr1) > len(arr2):
        for i in arr1:
            for j in arr2:
                if i == j:
                    commonElements.append(i)
    else:
        for i in arr2:
            for j in arr1:
                if i == j:
                    commonElements.append(i)
    return commonElements
"""
def getSetOf(message):
    messageSet: set = set()
    j = -1
    for i in range(0, len(message)):
        if message[i] == ' ':
            subString = message[j + 1: i]
            j = i
            messageSet.add(subString)
        elif i == len(message) - 1:
            subString = message[j + 1: i + 1]
            messageSet.add(subString)
    return messageSet

def getArrOfWords(str):
    arr = []
    j = -1
    for i in range(0, len(str)):
        if str[i] == ' ':
            subString = str[j + 1: i]
            j = i
            arr.append(subString)
        elif i == len(str) - 1:
            subString = str[j + 1: i + 1]
            arr.append(subString)
    return arr

def getFreqencyDict(arrOfWords):
    dict = {}
    for words in arrOfWords:
        count = 1
        if words not in dict:
            dict[words] = count
        elif words in dict:
            count += 1
            dict[words] = count
    return dict

