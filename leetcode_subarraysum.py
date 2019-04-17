class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if S == 0 & sum(A)==0:
            ret = len(A)+sum(range(len(A)))
    return ret



        ret =0
        for i in range(len(A)):
            for k in range(S,len(A)+1):
                if len(A[i:i+k])==0 : continue
                if sum(A[i:i+k])==S:
                    ret+=1
                    print A[i:i+k], i,i+k
                    if (i+k)==len(A):
                        break
        return ret


def main():
    A= [0,0,0,0,0]
    S= 0
    ret = Solution().numSubarraysWithSum(A,S)


if __name__ == '__main__':
    main()