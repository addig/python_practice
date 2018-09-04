def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    print s1==s2


def anagram(s1,s2):
    d = {}
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False

    for l in s1:
        if l in d:
            d[l] += 1
        else:
            d[l] =1

    for l in s2:
        if l in d:
            d[l] -= 1
        else:
            d[l] =1

    for l in d:
        if d[l] !=0:
            return False
    return True



anagram('dogogogogo','godgggoooo')

anagram('clint eastwood','old west action')

anagram('aa','bb')