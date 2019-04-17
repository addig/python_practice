def unique_char(s):
    """

    :param s:
    :return:
    """

    seen =[]
    for i in s:
        if i not in seen:
            seen = seen + [i]
        else:
            return False

    return True

F=unique_char("abcde")
print F