
"""n = 8
s = 'UDDDUDUU'
startStep = s[0]
count = 0
v = 0
for i in range(n):
    if s[i] == 'U':
        count += 1
    else:
        count -= 1
    if count == 0:
        if startStep == 'D':
            v += 1

        if i <n-1:
            startStep = s[i+1]
    else:
        pass
print v


def jumpingOnClouds(c):
    # 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0
    j = len(c) - 1  # 17
    countZero = 0
    flagzero=0
    for i in range(len(c)):  # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        if c[i] == 0:
            countZero += 1
            if flagzero == 1:
                countZero+=1
                flagzero = 0


            if countZero == 3:
                j -= 1
                countZero = 0
                flagzero= 1
        else:
            j -= 1
            countZero = 0
            flagzero = 0
    return j



dd= jumpingOnClouds([0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0])
#dd= jumpingOnClouds([0,0,0,0,0,0,0,1,0])
"""

def equalizeArray(arr):
    arr.sort()
    ele = list(set(arr))
    start = 0

    for e in ele:
        n = arr.count(e)
        if n >= start:
            start = n

    return (len(arr)-start)

    print arr


equalizeArray([1,2, 3, 1, 2, 3, 3, 3])