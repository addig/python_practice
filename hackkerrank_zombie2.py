class Solution(object):

    def __init__(self):
        # self.zombies = zombies
        self.clusternum = 0
        # self.neighbormap = {} # debug

    def findNeighbors(self, i, j):
        right = None
        left = None
        top = None
        down = None
        if j < self.collen - 1:
            if self.checkZombies(i, j + 1):
                right = 'z' + str(i) + str(j + 1)
        if j > 0:
            if self.checkZombies(i, j - 1):
                left = 'z' + str(i) + str(j - 1)
        if i > 0:
            if self.checkZombies(i - 1, j):
                top = 'z' + str(i - 1) + str(j)
        if i < self.rowlen - 1:
            if self.checkZombies(i + 1, j):
                down = 'z' + str(i + 1) + str(j)
        key = 'z' + str(i) + str(j)
        # self.neighbormap[key] = {right,left,top,down} #debug
        return {key}, {right, left, top, down}

    def checkZombies(self, i, j):
        return True if self.zombies[i][j] == 1 else False

    def zombiecluster(self, zombies):
        self.zombies = zombies
        B = set()

        self.rowlen = len(self.zombies[0])
        self.collen = len(self.zombies)

        for i in range(self.rowlen):
            for j in range(self.collen):
                if self.checkZombies(i, j):
                    key, A = self.findNeighbors(i, j)
                    if (A == {None}):
                        self.clusternum += 1
                    else:
                        C = (A | key) & (B)
                        if (C == {None}):
                            self.clusternum += 1
                        B = A | key
        if C != set():
            self.clusternum += 1
        return self.clusternum


def main():
    n = 6
    # zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
    zombies = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    zombies = [[0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0]]
    # zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[1,0,0,1]]
    # zombies = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
    # zombies = [[1,1,0,0],[0,1,0,0],[0,0,1,0],[1,0,1,1]]

    ret = Solution().zombiecluster(zombies)
    print ret

    print ret


if __name__ == '__main__':
    main()
