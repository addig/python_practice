class Solution(object):
    def zombiecluster(self,zombies):
        clusternum = 0
        self.zombies = zombies

        z_count = [z.count(1) for z in zombies]
        print 1


        return clusternum


def main():
    n = 6
    zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]

    ret = Solution().zombiecluster(zombies)


    print ret
if __name__ == '__main__':
    main()