def GCD(m, n):
    q = int(m / n)
    r = m - n * q
    return r

def LCM(m, n):
    tempM = abs(m*n)
    while GCD(m, n) != 0:
        tempR = GCD(m, n)
        m, n = n, tempR
    lcm = int(tempM/tempR)
    return lcm