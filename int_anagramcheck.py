def checkAnagram(s1,s2):
    """

    :param s1: string 1
    :param s2: string 2
    :return: n=boolean
    """
    import re
    s1 = s1.replace(" ","").
    """
    s1 = re.sub(" +","",s1).lower()
    s2 = re.sub(" +","",s2).lower()

    if len(s1) == len(s2):

        l1 = set([x for x in s1])
        l2 = set([x for x in s2])
        res = l1.intersection(l2)
        if len(res) == len(l1):
            return True
        else:
            False
    else:
        return False
        
    """



s1 = "public relations"
s2 = "crap built on lies"
checkAnagram(s1,s2)