def minimumBribes(q):
    p1 = 1
    p2 = 2
    p3 = 3
    bribes = 0
    for i in range(0, len(q)):
        if q[i] == p1:
            p1 = p2
            p2 = p3
            p3 += 1
        elif q[i] == p2:
            p2 = p3
            p3 += 1
            bribes += 1
        elif q[i] == p3:
            p3 += 1
            bribes += 2
        else:
            print("Too chaotic")
            return
    print(bribes)




    """ individualBribes = {}
    bribes = 0
    isChaotic = False
    tempQ = [i for i in q]
    tempQ.sort()
    isSorted = False
    while isSorted == False:
        for i in range(0, len(q) - 1):
            if q[i] > q[i + 1]:
                if q[i] not in individualBribes:
                    individualBribes[q[i]] = 1
                else:
                    individualBribes[q[i]] += 1
                if individualBribes[q[i]] > 2:
                    print("Too chaotic")
                    isChaotic = True
                    return
                swap(q, i, i + 1)
                bribes += 1
            if tempQ == q:
                isSorted = True
    if not isChaotic:
        return bribes"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp