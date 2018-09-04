def rotLeft(a, d):
    n = len(a)
    rotend= a[0:d]
    rotfront = a[d:n]
    return rotfront+rotend
    print 1

if __name__ == '__main__':

    a= [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
    d = 10
    result = rotLeft(a, d)
    print result
