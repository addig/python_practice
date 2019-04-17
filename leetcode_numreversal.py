class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ll = pow(-2,31)
        ul = pow(2,31)-1
        num = str(x)
        rev  =""
        for i in range(len(num)):
            rev = num[i]+rev
        if rev[-1] =='-':
            rev = '-' + rev[:-1]
        if (int(rev) > ll) & (int(rev)<ul):
            return int(rev)
        else:
            return 0


def main():

    x =-7654321

    ret = Solution().reverse(x)

    print ret

if __name__ == '__main__':
    main()


