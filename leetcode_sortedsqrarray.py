


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x*x for x in A])


    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        from math import log, ceil
        ret = []

        #maxi =int(bound/x)
        maxi = int(ceil(log(bound,x)))
        maxj = int(ceil(log(bound,y)))
        for i in range(maxi):
            for j in range(maxj):
                if pow(x,i) + pow(y,j)<=bound:
                    ret = ret + [pow(x,i) + pow(y,j)]
                else:
                    break

        ret = list(set(ret))

        return  ret

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l = len(pairs)
        pairchain = []
        for k in range(l):
            count = 1
            fw = l-k
            bw = k
            for i in range(1, fw):
                if pairs[k][1] < pairs[k + i][0]:
                    count += 1
            for j in range(bw,0,-1):
                if pairs[k][1]<pairs[k-j][0]:
                    count+=1

            pairchain = pairchain + [count]
        return max(pairchain)


def main():

    A = [-3,-2,1,4,10]
    pairs =[[5, 6], [3, 4], [1, 2]]
    #ret = Solution().sortedSquares(A)
    #ret = Solution().powerfulIntegers(2,3,10)
    ret = Solution().findLongestChain(pairs)

    print ret

if __name__ == '__main__':
    main()


