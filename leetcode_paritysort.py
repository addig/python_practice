class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_lst = []
        odd_list = []
        for i in A:
            if i%2 == 0:
                even_lst.append(i)
            else:
                odd_list.append(i)

        return even_lst+odd_list


def main():

    A = [3,1,2,4]

    ret = Solution().sortArrayByParity(A)

    print ret

if __name__ == '__main__':
    main()


