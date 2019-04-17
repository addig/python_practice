import sys

#x =sys.argv[1]

#for i in range(int(x)):#
 #  print i


y = int(input("How many candies do you want"))

for j in range(y):
    print "candy"


c=[0,0,0,0,1,0,0]
j=len(c)
countZero=0
for i in range(len(c)):
    if c[i]==0:
        countZero+=1
        if countZero == 3:
            j-=1
    else:
        j-=1
        countZero = 0
print j