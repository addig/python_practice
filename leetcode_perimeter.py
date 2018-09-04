class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        area = 0
        for i in range(row):
            for k in range(col):
                if grid[i][k]==1:
                    subarea = 4
                #find number of neighbors
                    numn = 0
                    if grid[i-1][k]==1:
                        numn+=1
                    subarea = subarea - numn
                    area = area +subarea

        return area



def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():

    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

    ret = Solution().islandPerimeter(grid)

    out = intToString(ret)
    print out


if __name__ == '__main__':
    main()