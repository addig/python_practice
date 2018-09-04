class Solution(object):
    def __init__(self):
        alpha = map(chr, range(ord('a'), ord('z') + 1))
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",\
                 "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.alphabet_ref = dict(zip(alpha, morse))
        self.x_word = []
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for word in words:
            t = ""
            for l in word:
                t = t + self.alphabet_ref[l]
            self.x_word.append(t)
        num = len(set(self.x_word))
        return num



def stringToStringArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    words = ["gin", "zen", "gig", "msg"]
    ret = Solution().uniqueMorseRepresentations(words)

    out = intToString(ret)
    print out


if __name__ == '__main__':
    main()

#