class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for row in A:
            L = len(row)
            new_row = []
            j = L-1
            for k in range(0,L):
                new_row.append(1-(row[L-1-k]))
            B.append(new_row)
        return B




def main():
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    ret = Solution().flipAndInvertImage(A)

    out = ret
    print out
    print 1


if __name__ == '__main__':
    main()