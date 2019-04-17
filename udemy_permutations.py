
def permute(s):

    """

    :param s:
    :return:

    a, bc cb| b ac ca | c ab ba

    """
    out = []
    if len(s) == 1:
         out = [s]
    else:
        for i,l in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [l + perm]
    return out

def coinChange(amount,coins):

    count = 0
    newAm    = amount
    while newAm!=0:
        if not coins:
            return -1
        newAm = newAm -  max(coins)
        if newAm >0:
            count +=1
        elif newAm<min(coins):
            newAm+=max(coins)
            coins.remove(max(coins))

        else:
            count+=1
            break
    return count


ccc = coinChange(6249,[186,419,83,408])

s = 'abc'

sorted

list_perm = permute(s)

print list_perm