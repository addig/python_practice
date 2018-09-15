class Solution(object):
    def __init__(self,zombies):
        self.zombies = zombies
    def checkzombies(self, i, j):
        return True if self.zombies[i][j]==1 else False

    def zombiecluster(self):

        z_count = sum(z.count(1) for z in self.zombies)
        clusternum = 1 if z_count>=1 else 0

        rowlen = len(self.zombies[0])
        collen = len(self.zombies)
        imem = -1
        jmem = -1
        hitzero= False

        #             0 1 2 3
        #zombies = [0[1,0,0,1],
        #           1[0,1,1,0],
        #           2[0,1,1,0],
        #           3[1,0,0,1]]
        for j in range(collen):
            i=0
            jrestore = j
            nextcolflag = False
            while i < rowlen : # i = 1 j = 1, nextcolflag = F, clusternum = 2 , jrestore = 1
                if self.checkzombies(i, j) :
                    if nextcolflag ==False:
                        i+=1
                        if hitzero:
                            clusternum+=1
                            hitzero = False

                    else :
                        if i >0:
                            i-=1
                        else:
                            break
                        if not self.checkzombies(i,j):
                            if (i+1!= imem) & (j!=jmem):
                                clusternum +=1
                                imem = i+1
                                jmem = j
                        else:
                            hitzero= True
                             #   rowlen-=1
                        nextcolflag = False
                        i+=2
                        j=jrestore



                else:
                    if not nextcolflag:
                        jrestore = j

                    if j< collen-1:
                        j+=1
                        nextcolflag = True
                    else:
                        break



        print 1


        return clusternum


def main():
    n = 6
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    #zombies = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[1,0,0,1]]
    zombies = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]

    ret = Solution(zombies).zombiecluster()
    print ret

    print ret
if __name__ == '__main__':
    main()