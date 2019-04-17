class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lenA = len(A)
        N = lenA/2
        sumA = sum(A)
        sumB = sum(set(A))
        ret = (sumA - sumB)/(N-1)
        return ret



def main():
    A = [2,1,2,5,3,2]
    ret = Solution().repeatedNTimes(A)
    print ret


if __name__ == '__main__':
    main()