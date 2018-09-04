class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        print right
        print left
        """l=[]
        for i in range(left, right+1):
            flag = True
            for digit in str(i):
                if int(digit) != 0:
                    if i % int(digit) != 0:
                        flag = False
                else:
                    flag = False

            if flag == True:
                l.append(i)
        return l"""

        def test(num):
            x = num
            while x > 0:
                if x % 10 == 0 or (num % (x % 10)) != 0:
                    return False
                x /= 10
            return True

        return list(filter(test, range(left, right + 1)))


def main():
    left = 500
    right = 650

    ret = Solution().selfDividingNumbers(left, right)
    print ret



if __name__ == '__main__':
    main()