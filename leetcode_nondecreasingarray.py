class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        checkflag = True
        count = 0
        for i in range(N-1,-1,-1):
            if nums[i]> nums[i-1]:
                checkflag = checkflag and True
            else:
                checkflag = checkflag and False
                count+=1
                if count >1:
                    return checkflag
            if checkflag ==False and count==1:



        #print checkflag
        return checkflag
def main():
    nums= [2,9,7]
    ret = Solution().checkPossibility(nums)
    print ret


if __name__ == '__main__':
    main()