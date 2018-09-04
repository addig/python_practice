class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flag = True
        nd =[]
        numC = 0
        while flag:
            d = num%2
            num = num/2
            if num  ==0:
                flag = False
            nd = nd+ [(1-d)]
        for i in range(len(nd)):
            numC+=nd[i]*pow(2,i)

        return numC

def main():
    num =14

    ret = Solution().findComplement(num)


    print ret
if __name__ == '__main__':
    main()