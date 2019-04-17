

def findNeighbors(zombies_mat, i, j):
    rowlen = len(zombies_mat[0])
    collen = len(zombies_mat)
    right = None
    left = None
    top= None
    bottom = None
    if j<collen-1:
        if checkZombies(zombies_mat,i,j+1):
            right = 'z'+str(i)+str(j+1)
    if j>0:
        if checkZombies(zombies_mat,i,j-1):
            left = 'z' + str(i) + str(j-1)
    if i>0:
        if checkZombies(zombies_mat,i-1,j):
            top='z'+str(i-1)+str(j)
    if i<rowlen-1:
        if checkZombies(zombies_mat,i+1,j):
            bottom='z'+str(i+1)+str(j)
    key = 'z'+str(i)+str(j)
    #neighbormap[key] = {right,left,top,bottom} #debug
    return {key}, {right, left, top, bottom}

def checkZombies(zombies_mat, i, j):
    return True if zombies_mat[i][j]==1 else False

def zombiecluster(zombies):
    zombies_mat = getZombies(zombies)
    clusternum = 0


    B = set()

    rowlen = len(zombies_mat[0])
    collen = len(zombies_mat)

    for i in range(rowlen):
        for j in range(collen):
            if checkZombies(zombies_mat,i,j):
                key, A = findNeighbors(zombies_mat,i,j)
                if (A == {None}):
                    clusternum+=1
                else:
                    C = (A|key) & (B)
                    if (C == {None}):
                        clusternum+=1
                    B= A|key
    if C!=set():
        clusternum += 1

    return clusternum

def getZombies(zombies):
    zombies_mat =[]
    for i in zombies:
        z=[]
        for k in range(len(i)):
            z = z+([int(i[k])])
        zombies_mat = zombies_mat+[z]
    return zombies_mat




def main():
    n = 6

    zombies = ['1100', '1110', '0110', '0001']

    ret = zombiecluster(zombies)
    print ret

    print ret
if __name__ == '__main__':
    main()