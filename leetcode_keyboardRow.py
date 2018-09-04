class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret=[]
        q = ['q','w','e','r','t','y','u','i','o','p']
        a = ['a','s','d','f','g','h','j','k','l']
        z = ['z','x','c','v','b','n','m']
        for word1 in words:
            flag = False
            word=word1.lower()
            if word[0] in q:
                keyboardRow = q

            elif word[0] in a:
                keyboardRow = a
            else:
                keyboardRow = z

            for i in range(len(word)):
                if word[i] in keyboardRow:
                    flag = True
                else:
                    flag = False
                    break
            if flag ==True:
                ret = ret+[word1]

        return ret



def main():

    words = ["Hello", "Alaska", "Dad", "Peace"]

    ret = Solution().findWords(words)


    print ret


if __name__ == '__main__':
    main()