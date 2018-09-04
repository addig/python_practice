class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        self.bin = []
        convertbin(self.bin, x^y)
        dist = sum(self.bin)
        # dist = bin(x^y).count('1')
        return dist

def convertbin(nbin,n):
    if n >1:
        convertbin(nbin,n//2)
    nbin = nbin.append(n%2)



def convertToBinary(n,a):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2,a)
   a = a.append(n%2)




def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    x = 1
    y = 4
    ret = Solution().hammingDistance(x, y)

    out = intToString(ret)
    print out



if __name__ == '__main__':
    main()