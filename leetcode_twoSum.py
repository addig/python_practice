class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.l = len(nums)
        self.nums = nums
        self.target = target
        self.ind = [0,0]
        for i in xrange(self.l):
            for k in xrange(i+1,(self.l)):
                sum_num = nums[i]+nums[k]
                if sum_num == self.target:
                    self.ind = [i,k]
                    return self.ind


if __name__ == "__main__":
    nums = map(int, raw_input().split(","))
    target = int(raw_input())
    sol = Solution()
    index = sol.twoSum(nums, target)

    print index

    print 1


#########Leetcode codeway

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.l = len(nums)
        self.nums = nums
        self.target = target
        self.ind = [0, 0]
        for i in xrange(self.l):
            for k in xrange(i + 1, (self.l)):
                sum_num = nums[i] + nums[k]
                if sum_num == self.target:
                    self.ind = [i, k]
                    return self.ind


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            line = lines.next()
            target = stringToInt(line)

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()