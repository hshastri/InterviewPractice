from Fib import *
from StairCase import *
from IceParlor import *
from MakeChange import *
from Anagram import *
from KnapSack import *
from CountValley import *
from JumpingClouds import *
from Pairs import *
from RepeatedString import *
from RotateLeft import *
from MinimumBribes import *
from MinSwaps import *
from RansomNote import *
from MaximumToys import *
from SherlockAnagram import *

def main():

    print("Fibonacci problem")
    print(Fib(30))  # too slow to calculate fib(300) for example
    print(FibBottomUp(300))
    print(FibMemo(300))
    print()

    print("Staircase Problem")
    print(countPaths(10))
    print(countStairsBottomUp(10))
    print(countPathsMemo(10))
    print(countPathSpaceOptimized(10))
    print()

    print("Ice Cream Parlor Problem")
    arr = [1,3,5,6,8,2,7]
    print(IceCreamParlor(arr, 10))
    print()

    print("Make Change")
    coins = [1,2,5]
    amount = 5
    print(MakeChange(coins, amount))
    print()

    print("Anagram Problem")
    str1 = "Helllo"
    str2 = "Billion"
    strA = "Harsh"
    strB = "Ryan"
    print(findAnagram(str1, str2))
    print(findAnagram(strA, strB))
    print(findAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
    print()

    print("Knapsack Problem")
    knapSack = {5: 60, 3:50, 4:70, 2:30}
    weight = 5
    print(KnapSack(knapSack, weight))

    print("Count Valley")
    print(countingValleys(8,"UDDDUDUU"))
    print()

    print("Jumping Clouds")
    print(jumpingOnClouds([0,0,0,1,0,0]))
    print()

    print("Pairs")
    ar = [4,5,5,5,6,6,4,1,4,4,3,6,6,3,6,1,4,5,5,5]
    print(sockMerchant(len(ar), ar))
    print()

    print("Repeated String")
    print(repeatedString("abc", 10))
    print()

    print("Rotate Left")
    a = [1,2,3,4,5]
    print(rotLeft(a, 4))
    print()

    print("Minimum Bribes")
    q = [2, 1, 5, 3, 4]
    minimumBribes(q)
    print()

    print("Minimum Swaps")
    arr = [1,3,5,2,4,6,7]
    print(minimumSwaps(arr))
    print()

    print("Ransom Note")
    magazine = "give me one grand today night"
    note = "give me one grand today"
    magazine2 = "two times three is not four"
    note2 = "two times two is four"
    magazine3 = "ive got a lovely bunch of coconuts"
    note3 = "ive got some coconuts"
    magazine4 = "I will not kill you"
    note4 = "I will kill you"
    note5 = "I will kill kill you"
    checkMagazine(magazine, note)
    checkMagazine(magazine2, note2)
    checkMagazine(magazine3, note3)
    checkMagazine(magazine4, note4)
    checkMagazine(magazine4, note5)
    print()

    print("Maximum Toys")
    prices = [33324560, 77661073, 31948330, 21522343, 97176507, 5724692, 24699815, 12079402, 6479353, 28430129, 42427721, 57127004, 26256001, 29446837, 65107604, 9809008, 65846182, 8470661, 13597655, 360]
    k = 100000
    print(maximumToys(prices, k))
    print()

    print("Sherlock Anagrams")
    s = "abba"
    print(sherlockAndAnagrams(s))


if __name__ == '__main__':
    main()
