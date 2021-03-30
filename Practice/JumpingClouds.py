def jumpingOnClouds(c):
    jumps = 0
    return jumpingOnCloudsHelper(c, jumps)

def jumpingOnCloudsHelper(c, jumps):
    currentCloud = 0

    if len(c) <= 3:
        if len(c) == 1:
            return jumps
        elif len(c) == 2:
            if c[currentCloud + 1] == 0:
                jumps += 1
                return jumps
        elif len(c) == 3:
            if c[currentCloud + 2] == 0 or c[currentCloud + 1] == 0:
                jumps += 1
                return jumps

    if c[currentCloud + 2] != 1:
        jumps += 1
        currentCloud += 2
        return jumpingOnCloudsHelper(c[currentCloud:], jumps)
    elif c[currentCloud + 2] == 1 and c[currentCloud + 1] != 1:
        jumps += 1
        currentCloud += 1
        return jumpingOnCloudsHelper(c[currentCloud:], jumps)