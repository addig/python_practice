def reverseString(s):
    if not s:
        return ""
    else:
        return s[-1]+reverseString(s[0:-1])


def fact(num):
    if num ==0:
        return 1
    else:
        return num*fact(num-1)

def word_split(phrase, list_of_words, output=None):
    return [x for x in list_of_words if x in phrase]


def perm(s):
    # base case
    if not s:
        pass
    # recursion
    else :
        s1 =s[0]+s[1:]

        p = [s1]+perm(s1)
    return p


perm('abc')

d = word_split('ilovetheJohn',['i','am','a','dogs','lover','love','John'])
print fact(5)

print reverseString('abc')
print 1

'cba'