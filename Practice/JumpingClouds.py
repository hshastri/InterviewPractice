def jumpingOnClouds(c):
    jumps = 0
    return jumpingOnCloudsHelper(c, jumps)

def jumpingOnCloudsHelper(c, jumps):
    currentCloudIndex = 0

    """
        If there's only one cloud left, since the c[0] = c[n - 1] = 0 always, just return jumps. If there are two clouds left, and since c[n - 1] = 0, it is always possible to take a leap and return the jumps after incrementing the jumps variable. Also if there are three clouds left, the last cloud is always gonna be 0 since c[n-1] = 0, so take two leaps at a time, increment jumps by one and return jumps
    """
    if len(c) <= 3:
        """
        if len(c) == 3:
            if c[currentCloudIndex + 1] == 0 or c[currentCloudIndex + 2] == 0:
                jumps += 1
                return jumps
        if len(c) == 2:
            if c[currentCloudIndex + 1] == 0:
                jumps += 1
                return jumps"""
        if len(c) == 1:
            return jumps
        else:
            jumps += 1
            return jumps

    if c[currentCloudIndex + 2] != 1:
        jumps += 1
        return jumpingOnCloudsHelper(c[currentCloudIndex + 2:], jumps)
    elif c[currentCloudIndex + 2] == 1 and c[currentCloudIndex + 1] == 0:
        jumps += 1
        return jumpingOnCloudsHelper(c[currentCloudIndex + 1:], jumps)
