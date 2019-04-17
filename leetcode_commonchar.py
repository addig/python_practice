class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        next_set = set(A[0])
        for x in A:
            next_set = set(x) & next_set

        return list(next_set)



A = ["bella","label","roller"]

ret = Solution().commonChars(A)