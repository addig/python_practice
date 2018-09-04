class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        lst_c = [pos for pos, char in enumerate(S) if char == C] #S.index(C)
        lst = range(len(S))
        dct= []
        for ind in lst_c:
           dct = dct+[[abs(num-ind) for num in lst]]

        ret=[]
        for j in lst:
            temp = 9999999
            for i in range(len(lst_c)):
                temp = min(temp,dct[i][j])
            ret = ret+[temp]
        return ret


        print dct





def main():

    S = "loveleetcode"
    C = "e"
    ret = Solution().shortestToChar(S, C)

    print ret

if __name__ == '__main__':
    main()

#Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]