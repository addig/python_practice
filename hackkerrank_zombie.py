class Solution(object):
    def zombiecluster(self,zombies):
        clusternum = 0
        self.zombies = zombies
        left = False
        right = False
        up = False
        down = False
        nextcolflag = False
        rowlen = len(zombies[0])
        collen = len(zombies)
        i = 0
        j = 0
        jrestore = None
        #zombies = [[1,1,0,0],
        #           [1,1,1,0],
        #           [0,1,1,0],
        #           [0,0,0,1]]
        for j in range(collen):
            i=0
            while i < rowlen : # i = 2, j = 0, nextcolflag = T, clusternum = 0 , jrestore = 0
                if zombies[i][j] == 1 :
                    if nextcolflag ==False:
                        i+=1

                    else :
                        i-=1
                        if nextcolflag ==True:
                            clusternum +=1
                            nextcolflag = False
                            i+=1
                            j=jrestore
                else:
                    jrestore = j
                    j+=1
                    nextcolflag = True


        z_count = [z.count(1) for z in zombies]
        print 1


        return clusternum


def main():
    n = 6
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
    zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]

    ret = Solution().zombiecluster(zombies)


    print ret
if __name__ == '__main__':
    main()