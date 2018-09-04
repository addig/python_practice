class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        colN = len(A[0])
        rowN = len(A)
        L2 =[]
        for i in xrange(colN):
            L1 =[]
            for j in xrange(rowN):
                L1.append(A[j][i])
            L2.append(L1)

        return L2




def main():
    A =[[1, 2], [4, 5],[7,8]]

    ret = Solution().transpose(A)

    out = ret
    print out



if __name__ == '__main__':
    main()