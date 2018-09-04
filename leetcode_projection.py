import numpy as np
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        proj =0
        top = np.count_nonzero(grid)
        colside = 0
        rowside = 0
        for i in range(len(grid[0])):
            colside+= max(grid[i])
            lst =[]
            for j in range(len(grid)):
                lst = lst+[grid[j][i]]
            rowside+=max(lst)
        proj = top+colside+rowside
        return proj


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    # grid = [[1,0],[0,2]] # [[1,1,1],[1,0,1],[1,1,1]] # [[2,2,2],[2,1,2],[2,2,2]]
    #grid = [[1,1,1],[1,0,1],[1,1,1]] # [[2,2,2],[2,1,2],[2,2,2]]
    grid = [[2,2,2],[2,1,2],[2,2,2]]

    ret = Solution().projectionArea(grid)

    out = intToString(ret)
    print out


if __name__ == '__main__':
    main()