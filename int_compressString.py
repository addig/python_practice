def compressString(s):
    """

    :param s:
    :return:
    """

    count = 1
    length = len(s)
    i = 1
    newS = ''

    while i < length:
        if s[i] == s[i-1]:
            count+=1
        else:
            newS= newS+s[i-1]+str(count)
            count  =1
        i+=1

    newS = newS + s[i-1] + str(count)

    #s1 = list(set(s))
    #for i in s1:

    return newS


newS = compressString("AAAAaaaccc")
print newS