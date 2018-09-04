class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        return A.index(max(A))


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    A = [0, 2,3,1, 0]
    ret = Solution().peakIndexInMountainArray(A)
    out = intToString(ret)
    print 1



if __name__ == '__main__':
    main()