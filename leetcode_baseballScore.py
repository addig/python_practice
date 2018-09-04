class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        lst = []
        for cd in ops:
            if cd == 'C':
                lst.pop(-1)
            elif cd == 'D':
                lst = lst+[2*lst[-1]]

            elif cd =='+':
                lst= lst+[lst[-1]+lst[-2]]

            else:
                lst = lst+ [int(cd)]

        return sum(lst)






def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():

    ops = ["5","-2","4","C","D","9","+","+"]

    ret = Solution().calPoints(ops)

    out = intToString(ret)
    print out



if __name__ == '__main__':
    main()