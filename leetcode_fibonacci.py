class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fiblist = [0,1]
        for i in range(2,N+1):
            next = fiblist[i-1]+fiblist[i-2]
            fiblist.append(next)

        return fiblist[N]


def main():
    N= 3
    ret = Solution().fib(N)
    print ret


if __name__ == '__main__':
    main()