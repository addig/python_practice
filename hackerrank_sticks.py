class Solution(object):
    def cutSticks(self, lengths):
        start_len = lengths[0]
        in_list = [start_len]
        arr = lengths[1::]

        while len(arr)>1:
            arr_updt = []
            minstick = min(arr)
            for i in arr:
                if i != minstick:
                    arr_updt = arr_updt +[(i-minstick)]
            new_len = len(arr_updt)
            arr = arr_updt
            in_list = in_list+[new_len]
        print in_list
        return in_list


def main():
    n = 6
    lengths = [6,5,4,4,2,2,8]

    ret = Solution().cutSticks(lengths)


    print ret
if __name__ == '__main__':
    main()