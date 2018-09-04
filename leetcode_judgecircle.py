class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # U=1
        # D=-1
        # L=2
        # R=-2
        # count = 0
        # for i in moves:
        #     if i=='U':
        #         count+=1
        #     elif i == 'D':
        #         count-=1
        #     elif i == 'L':
        #         count+=2
        #     else:
        #         count-=2
        # if count  ==0:
        #     return True
        # else:
        #     return False

        # udcount = (moves.count('U'))-(moves.count('D'))
        # LRcount = (moves.count('L'))-(moves.count('R'))
        # if (udcount==0) &(LRcount==0 ):
        #     return True
        # else:
        #     return False

        if (moves.count('U')==moves.count('D'))&(moves.count('L')==moves.count('R')):
            return True
        else:
            return False




def main():
    moves = "LDRRLRUULR"

    ret = Solution().judgeCircle(moves)

    out = (ret)
    print out

if __name__ == '__main__':
    main()