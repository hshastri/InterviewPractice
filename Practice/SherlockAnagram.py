def sherlockAndAnagrams(s):
    stringSet = set()
    for i in range(0, len(s)):
        stringSet.add(s[i])
    #frequency = getFrequencyDict(s)
    subStringArray = getSubStringArray(s)
    valueDict = getValueOfChars(stringSet)
    subArrNum = getSubArrayNum(subStringArray, valueDict)

    
def getSubArrayNum(subStringArray,valueDict):
    subArrNum = []
    for substring in subStringArray:
        subArrNum.append(stringValue(valueDict, substring))
    return subArrNum

def stringValue(valueDict, s):
    total = 0
    for char in s:
        total += valueDict[char]
    return total



def getValueOfChars(stringSet):
    dict = {}
    value = 1
    for char in stringSet:
        dict[char] = value
        value += 1
    return dict


def getSubStringArray(s):
    subStringArray = []
    for i in range(0, len(s)):
        if i == 0:
            continue
        else:
            subStringArray.append(s[0:i])
    return subStringArray

def getFrequencyDict(stringSet):
    dict = {}
    for char in stringSet:
        count = 1
        if char not in dict:
            dict[char] = count
        elif char in dict:
            dict[char] += 1
    return dict


