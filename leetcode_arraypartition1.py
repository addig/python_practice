### Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as
# large as possible.


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        numlist = sorted(nums)
        i=0
        pair = 0
        while i<=2*n-2:
            pair = pair + min([numlist[i],numlist[i+1]])
            i+=2
        return pair




def main():

    nums = [1, 4, 3, 2]
    ret = Solution().arrayPairSum(nums)

    print ret


if __name__ == '__main__':
    main()