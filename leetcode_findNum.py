class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        print matrix
        # Find maxCol, maxRow
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target in matrix[i]:
                return True
            else:
                pass

        return False





matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 25
ret = Solution().searchMatrix(matrix, target)
print ret