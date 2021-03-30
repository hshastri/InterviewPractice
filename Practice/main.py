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
    str1 = "Hello"
    str2 = "Billion"
    strA = "Harsh"
    strB = "Ryan"
    print(findAnagram(str1, str2))
    print(findAnagram(strA, strB))
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

if __name__ == '__main__':
    main()
