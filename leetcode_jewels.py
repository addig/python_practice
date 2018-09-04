class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        import re
        self.J = J
        self.S = S
        self.count = 0

        for j in self.J:
            for s in self.S:
                if j == s:
                    self.count += 1

        return self.count

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    J = "aA"
    S =  "aAAbbbb"

    ret = Solution().numJewelsInStones(J, S)

    out = intToString(ret)
    print out



if __name__ == '__main__':
    main()